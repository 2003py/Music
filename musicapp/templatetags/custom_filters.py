from django import template
import os

register = template.Library()

@register.filter
def file_extension_equals(value, arg):
    if value is None:
        return False
    file_extension = os.path.splitext(value)[1].lower()
    return file_extension == arg.lower()