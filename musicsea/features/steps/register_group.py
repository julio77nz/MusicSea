from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

use_step_matcher("parse")


@given('Exists group registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from musicseaapp.models import Group
    for row in context.table:
        group = Group(user=user)
        for heading in row.headings:
            setattr(group, heading, row[heading])
        group.save()


@when('I register group')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('musicseaapp:groups_create'))
        if context.browser.url == context.get_url('musicseaapp:groups_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@then('There are {count:n} groups')
def step_impl(context, count):
    from musicseaapp.models import Group
    assert count == Group.objects.count()


@then('I\'m viewing the details page for group by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from musicseaapp.models import Group
    group = Group.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(group)


@when('I edit the group with name "{name}"')
def step_impl(context, name):
    from musicseaapp.models import Group
    group = Group.objects.get(name=name)
    context.browser.visit(context.get_url('musicseaapp:group_edit', group.pk))
    if context.browser.url == context.get_url('musicseaapp:group_edit', group.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()
