from django import template

register = template.Library()

@register.filter(name="valuefor")
def valuefor(dict, key):
    try:
        return dict.get(key, '')
    except Exception as e:
        return ""
