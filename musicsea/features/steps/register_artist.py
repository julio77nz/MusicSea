from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists artist at group "{group_name}" by "{username}"')
def step_impl(context, group_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from musicseaapp.models import Group
    group = Group.objects.get(name=group_name)
    from musicseaapp.models import Artist
    for row in context.table:
        artist = Artist(group=group, user=user)
        for heading in row.headings:
            setattr(artist, heading, row[heading])
        artist.save()

@when('I register artist at group "{group_name}"')
def step_impl(context, group_name):
    from musicseaapp.models import Group
    group = Group.objects.get(name=group_name)
    for row in context.table:
        context.browser.visit(context.get_url('musicseaapp:artists_create', group.pk))
        if context.browser.url == context.get_url('musicseaapp:artists_create', group.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('I\'m viewing the details page for artist at group "{group_name}" by "{username}"')
def step_impl(context, group_name, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from musicseaapp.models import Group
    q_list.append(Q(('group', Group.objects.get(name=group_name))))
    from musicseaapp.models import Artist
    artist = Artist.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(artist)

@then('There are {count:n} artists')
def step_impl(context, count):
    from musicseaapp.models import Artist
    assert count == Artist.objects.count()

@when('I edit the current artist')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('musicseaapp:artist_edit', artist.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()
