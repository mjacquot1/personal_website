from django import template

# Needed to register the functions for template use
register = template.Library()

# Get passed a dictionary and key, return the key value
@register.filter
def return_key_value(dictionary_arg, filter_key):
    if dictionary_arg == None or filter_key == None:
        return
    
    if filter_key in dictionary_arg.keys():
        return dictionary_arg[filter_key]