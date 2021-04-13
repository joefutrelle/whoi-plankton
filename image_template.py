#env = Environment(
#    loader=FileSystemLoader('yourapplication', 'template'),
#    autoescape=select_autoescape(['html'])
#)
import jinja2
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader, Template

templateLoader = jinja2.FileSystemLoader(searchpath="templates")


autoescape = select_autoescape(['html'])
templateEnv = jinja2.Environment(loader=templateLoader)
file = "child_template.html"
template = templateEnv.get_template(file)


plankton_images = template.render( images = [
    {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'}
])


print(plankton_images)

