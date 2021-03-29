from django import template

register = template.Library()


@register.simple_tag
def repeat(text, n):
    return [text.format(k) for k in range(n)]

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
