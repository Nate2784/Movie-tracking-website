from django import template
register = template.Library()

@register.filter
def first_word(value):
    return value.split(' ')[0]

@register.filter
def second_word(value):
    return value.split(' ')[1]
