from django import template

register = template.Library()

@register.filter(name="valuefor")
def valuefor(dict, key):
	try:
		return dict.get(key, '')
	except Exception as e:
		return ""

@register.filter
def get_range( value ):
  """
	Filter - returns a list containing range made from given value
	Usage (in template):

	<ul>{% for i in 3|get_range %}
	  <li>{{ i }}. Do something</li>
	{% endfor %}</ul>

	Results with the HTML:
	<ul>
	  <li>0. Do something</li>
	  <li>1. Do something</li>
	  <li>2. Do something</li>
	</ul>

	Instead of 3 one may use the variable set in the views
  """
  return range( value )
@register.filter(name="get_index")
def get_index(arr, index):
  try:
	  return arr[index]
  except Exception as e:
	  return ''
