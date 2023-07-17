from django import template

register = template.Library()


@register.filter(name='get_rus_name')
def get_rus_name(dict, key):
    if key:
        return dict.get(key)
