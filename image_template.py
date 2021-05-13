import os
import jinja2
from jinja2 import select_autoescape
from more_itertools import grouper
import pandas as pd

templateLoader = jinja2.FileSystemLoader(searchpath="templates")
autoescape = select_autoescape(['html'])
templateEnv = jinja2.Environment(loader=templateLoader)
file = "child_template.html"
template = templateEnv.get_template(file)
file = "class_template.html"
class_template = templateEnv.get_template(file)

df = pd.read_csv('IFCB_image_wiki.csv')
df = df.dropna(subset=['image'])
df['class'] = df['class'].str.strip()

exemplar_image_rows = df[df['Index_ROI'] == 1]

group_chunks = {}
class_chunks = {}

MAX_COLUMNS = 4

#Generating index page
for group_name, group_rows in exemplar_image_rows.groupby('group'):
    image_records = group_rows.to_dict('records')
    for image_record in image_records:
        url = image_record['image']
        basename = os.path.basename(url)
        image_name, extension = os.path.splitext(basename)
        image_record['path'] = f'images/{image_name}.jpg'
    group_chunks[group_name] = list(grouper(image_records, MAX_COLUMNS))

index_images = template.render(group_chunks=group_chunks)

output_file = 'docs/output.html'

with open(output_file, 'w') as fout:
    print(index_images, file=fout)

#Generating individual class pages
for class_name, class_rows in df.groupby('class'):
    class_image_records = class_rows.to_dict('records')
    for class_image_record in class_image_records:
        url = class_image_record['image']
        basename = os.path.basename(url)
        class_image_name, extension = os.path.splitext(basename)
        class_image_record['path'] = f'images/{class_image_name}.jpg'
    class_chunks[class_name] = list(grouper(class_image_records, MAX_COLUMNS))
for class_name in class_chunks:
    class_pages = class_template.render(class_chunks=class_chunks[class_name], class_name=class_name)
    class_page_output = "docs/" + class_name + ".html"
    with open(class_page_output, 'w') as fout:
        print(class_pages, file=fout)