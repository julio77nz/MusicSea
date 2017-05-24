from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists song at group "{group_name}" by "{username}"')
def step_impl(context, group_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from musicseaapp.models import Group
    group = Group.objects.get(name=group_name)
    from musicseaapp.models import Song
    for row in context.table:
        song = Song(group=group, user=user)
        for heading in row.headings:
            setattr(song, heading, row[heading])
        song.save()

@when('I register song at group "{group_name}"')
def step_impl(context, group_name):
    from musicseaapp.models import Group
    group = Group.objects.get(name=group_name)
    for row in context.table:
        context.browser.visit(context.get_url('musicseaapp:songs_create', group.pk))
        if context.browser.url == context.get_url('musicseaapp:songs_create', group.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@when('I register song at album "{album_name}"')
def step_impl(context, album_name):
    from musicseaapp.models import Album
    album = Album.objects.get(name=album_name)
    for row in context.table:
        context.browser.visit(context.get_url('musicseaapp:songs_create', album.pk))
        if context.browser.url == context.get_url('musicseaapp:songs_create', album.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('I\'m viewing the details page for song at group "{group_name}" by "{username}"')
def step_impl(context, group_name, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from musicseaapp.models import Group
    q_list.append(Q(('group', Group.objects.get(name=group_name))))
    from musicseaapp.models import Song
    song = Song.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(song)

@then('There are {count:n} songs')
def step_impl(context, count):
    from musicseaapp.models import Song
    assert count == Song.objects.count()

@when('I edit the current song')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('musicseaapp:song_edit', song.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()
