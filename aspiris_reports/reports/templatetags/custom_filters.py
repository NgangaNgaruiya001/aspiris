from django import template

register = template.Library()

@register.filter
def get_item(queryset, subdivision):
    return queryset.filter(subdivision=subdivision).first()

@register.filter
def subtract(value, arg):
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def lookup(data, key):
    """
    Retrieves a value from a dictionary using a dynamically constructed key.
    The key can be passed as a string directly or concatenated dynamically in the template.
    """
    if isinstance(data, dict) and key in data:
        return data[key]
    return ''

@register.filter
def groupby(value, arg):
    """Groups a list of dictionaries by a specified key."""
    sorted_list = sorted(value, key=lambda x: x[arg])  # Sort first by the key
    return groupby(sorted_list, key=lambda x: x[arg])