#env = Environment(
#    loader=FileSystemLoader('yourapplication', 'template'),
#    autoescape=select_autoescape(['html'])
#)
import jinja2
from jinja2 import select_autoescape
from more_itertools import grouper
import csv

templateLoader = jinja2.FileSystemLoader(searchpath="templates")


autoescape = select_autoescape(['html'])
templateEnv = jinja2.Environment(loader=templateLoader)
file = "child_template.html"
template = templateEnv.get_template(file)

image_list = []
images = []

with open('IFCB_image_wiki.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        file = row[0]
        image_row = row[0], row[1], row[2], row[3], row[4]
        if file == '1':
            image_list.append(image_row)
            images.append("{src':" + row[3] + ",'href': 'https://github.com/joefutrelle/whoi-plankton', 'title':" + row[2] + "}")

chunks = list(grouper(images, 3))

plankton_images = template.render(rows=chunks)

output_file = 'docs/output.html'

with open(output_file, 'w') as fout:
    print(plankton_images, file=fout)



# images = [
 #    {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton',
    #    'title': 'amoeba'},
        #   {'src': 'images/Apedinella/IFCB5_2017_036_121145_03566.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton',
    #    'title': 'Apedinella'},
        #   {'src': 'images/Calciopappus/IFCB1_2009_262_003744_06032.jpg',
    #    'href': 'https://github.com/joefutrelle/whoi-plankton', 'title': 'Calciopappus'},
        #   {'src': 'images/Chaetoceros_pennate/IFCB1_2010_078_185738_02724.jpg',
        #    'href': 'https://github.com/joefutrelle/whoi-plankton', 'title': 'Chaetoceros_pennate'},
    #   {'src': 'images/Corethron hystrix/IFCB5_2011_001_165030_05039.jpg',
    #    'href': 'https://github.com/joefutrelle/whoi-plankton', 'title': 'Corethron hystrix'},
        #   {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton',
    #   'title': 'amoeba'},
        #  {'src': 'images/Apedinella/IFCB5_2017_036_121145_03566.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton',
    #   'title': 'Apedinella'},
        #  {'src': 'images/Calciopappus/IFCB1_2009_262_003744_06032.jpg',
    #    'href': 'https://github.com/joefutrelle/whoi-plankton', 'title': 'Calciopappus'},
        #  {'src': 'images/Chaetoceros_pennate/IFCB1_2010_078_185738_02724.jpg',
    #   'href': 'https://github.com/joefutrelle/whoi-plankton', 'title': 'Chaetoceros_pennate'},
        #  {'src': 'images/Corethron hystrix/IFCB5_2011_001_165030_05039.jpg',
    #   'href': 'https://github.com/joefutrelle/whoi-plankton', 'title': 'Corethron hystrix'},
        #  {'src': 'images/amoeba/IFCB1_2013_302_163814_00313.jpg', 'href': 'https://github.com/joefutrelle/whoi-plankton',
#  'title': 'amoeba'},

#]
