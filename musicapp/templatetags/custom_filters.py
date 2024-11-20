from django import template
import os

register = template.Library()

@register.filter
def file_extension_equals(value, arg):
    """
    检查文件路径对应的文件扩展名是否等于给定的扩展名
    """
    if value is None:
        return False
    file_extension = os.path.splitext(value)[1].lower()
    return file_extension == arg.lower()