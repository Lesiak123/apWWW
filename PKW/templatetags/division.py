from django import template

from django.template import Library

register = template.Library()

@register.filter
def div(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def add_float(value, arg):
    return float(value) + float(arg)

@register.filter
def mult(value, arg):
    return float(value)*float(arg)

@register.filter
def get_range( value ):
    return range(value)

@register.filter
def get_dec2(value):
    return format(value, '.2f')