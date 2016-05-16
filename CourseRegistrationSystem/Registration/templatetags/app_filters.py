from django import template

register = template.Library()

@register.filter(name="valuefor")
def valuefor(dict, key):
    return dict.get(key, '')
