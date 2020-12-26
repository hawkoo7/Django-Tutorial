from django import template

register = template.Library()

def cut(val,arg):
    return value.replace(arg,'')

register.filter('cut',cut)
