import cgi
import uuid
import re
import fs
import logging
from io import BytesIO as iostream

def process(e):
    form = e['L_FORM_DATA']
    filename = uuid.uuid1().hex + re.findall('\.\w+$', form['img'].filename)[0]
    fs.local.save(iostream(form['img'].value), filename)
    e['L_HTTP_CONTENT'] = '/image/%s' % filename
    return True
    
