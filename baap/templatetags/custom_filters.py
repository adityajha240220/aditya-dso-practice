from django import template
register = template.Library()

@register.filter
def upper_case(value):
    return value.upper()

@register.filter
def preview(value, n=80):
    """Return first n chars"""
    try:
        n = int(n)
    except Exception:
        n = 80
    text = str(value)
    return (text[:n] + ("..." if len(text) > n else ""))
