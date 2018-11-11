from jinja2 import Template
from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader('Useful')
)
template = Template('Hello {{ name }} !')
html = template.render(name='guanxiaojue')
print html


