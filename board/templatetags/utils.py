from django import template

register = template.Library()


@register.filter(name='show_name')
def show_name(user):
    return user.last_name + user.first_name


@register.filter(name='brief')
def brief(msg):
    return msg[:30]