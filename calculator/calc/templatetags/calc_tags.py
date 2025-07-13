from django import template
import calc.views as views

register = template.Library()

@register.simple_tag()
def get_calculators():
    return views.CALCS

@register.inclusion_tag('calc/list_calculators.html')
def show_calculators(calc_selected=None):
    calc = views.CALCS
    return {'calcs': calc, 'calc_selected': calc_selected}
