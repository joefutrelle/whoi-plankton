import os

import pandas as pd
import requests

df = pd.read_csv('IFCB_image_wiki.csv')

urls = df.pop('image').dropna()

for url in urls:
    base_url, ext = os.path.splitext(url)
    image_id = os.path.basename(base_url)
    jpg_url = f'{base_url}.jpg'
    image_path = f'docs/images/{image_id}.jpg'
    if not os.path.exists(image_path):
        try:
            r = requests.get(jpg_url)
            with open(image_path, 'wb') as fout:
                fout.write(r.content)
            print(f'downloaded {jpg_url}')
        except:
            print(f'error downloading {jpg_url}')