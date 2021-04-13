from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader, Template

#env = Environment(
#    loader=FileSystemLoader('yourapplication', 'template'),
#    autoescape=select_autoescape(['html'])
#)

import jinja2

#templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateLoader = jinja2.FileSystemLoader(searchpath="/Users/mpeterson21/PycharmProjects/whoi-plankton2/templates/")


templateEnv = jinja2.Environment(loader=templateLoader)
file = "child_template.html"
template = templateEnv.get_template(file)



plankton_images = template.render(images = [
    {'src': 'docs/images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'docs/images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'docs/images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'docs/images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'docs/images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'},
    {'src': 'docs/images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton'}
])


print(plankton_images)

