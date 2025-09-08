# store/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='split_first')
def split_first(value, delimiter="|"):
    """Splits a string at the first occurrence of the delimiter and returns the first part."""
    if isinstance(value, str):
        return value.split(delimiter)[0].strip()
    return value  # return value if it's not a string
