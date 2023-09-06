from django import template
register = template.Library()

@register.filter
def to_number(value):
    return f"{value:,}"

@register.filter
def to_title(value):
    return value.title()
@register.filter
def to_mask(value):
    return "X"* (len(value)-4) + value[-4:]