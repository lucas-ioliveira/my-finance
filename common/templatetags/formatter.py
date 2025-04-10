from django import template
import re

register = template.Library()


@register.filter
def format_telefone(value):
    if not value:
        return ''

    value = re.sub(r'\D', '', value)

    if len(value) == 10:
        return f"({value[:2]}) {value[2:6]}-{value[6:]}"

    elif len(value) == 11:
        return f"({value[:2]}) {value[2:7]}-{value[7:]}"

    return value


@register.filter
def format_cep(value):
    if not value:
        return ""

    value = re.sub(r'\D', '', value)

    if len(value) == 8:
        return f"{value[:5]}-{value[5:]}"
    return value
