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

df = pd.read_csv('IFCB_image_wiki.csv')

df = df.dropna(subset=['image'])

exemplar_image_rows = df[df['Index_ROI'] == 1]

group_chunks = {}

MAX_COLUMNS = 3

for group_name, group_rows in exemplar_image_rows.groupby('group'):
    image_records = group_rows.to_dict('records')
    for image_record in image_records:
        url = image_record['image']
        basename = os.path.basename(url)
        image_name, extension = os.path.splitext(basename)
        image_record['path'] = f'images/{image_name}.jpg'
    group_chunks[group_name] = list(grouper(image_records, MAX_COLUMNS))


plankton_images = template.render(group_chunks=group_chunks)

output_file = 'docs/output.html'

with open(output_file, 'w') as fout:
    print(plankton_images, file=fout)