from common import default_header
from common import html_base
import os


class html_images(html_base):
    rf_base = ['title', 'header_attrs', 'body']
    rf_body = ['nav_bar', 'images']
    tp_base = 'webpage/base.html'
    tp_nav_bar = 'webpage/nav_bar.html'
    tp_body = 'webpage/images_body.html' 
    tp_image = 'webpage/images_image.html'

html = html_images()
html.title = 'Image Library'
image_template = html.get_template('tp_image')
image_path = '/data/image'

def process(e, r):
    header = default_header()
    html.images = '\n'.join([ image_template.format({'image_name': file_name, 'image_link': '/image/%s'% file_name}) for file_name in os.listdir(image_path)])
    content = html.get_result('tp_base', default='')
    return '200 ', header, content
    
