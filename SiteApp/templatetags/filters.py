from django import template

register = template.Library()


@register.filter(name='uppercase')
def uppercase(value):
    if value:
        return value.upper()
    return ''
