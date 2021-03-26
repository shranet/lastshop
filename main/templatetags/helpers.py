from django import template

register = template.Library()


@register.simple_tag
def repeat(text, n):
    return [text.format(k) for k in range(n)]
