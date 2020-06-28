from django import template

register = template.Library()

@register.inclusion_tag('ionicon.html')
def ionicon(*args, **kwargs):
    """
    Required: name
    Example: {% ionicon name="link-outline" %}
    """
    name = kwargs['name']
    return {'svg_file_path': f'./svgs/{name}.svg'}
