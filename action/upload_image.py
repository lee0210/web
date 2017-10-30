import db
import common
import os
import cgi
import uuid
import imp
import re

def process(e, r):
    header = common.default_json_header()
    form = cgi.FieldStorage(fp=e['wsgi.input'], environ=e)
    # validation
    inputs = ['captcha', 'img']
    if not len(inputs) == sum([x in inputs for x in form]):
        content = 'invalid request'
        return '200 ', header, content
    captcha = form['captcha'].value
    if common.check_captcha(captcha):
        filename = uuid.uuid1().hex + re.findall('\.\w+$', form['img'].filename)[0]
        path = '/data/image/{0}'.format(filename)    
        content = '/image/{0}'.format(filename)
        f = open(path, 'wb+')
        f.write(form['img'].value)
        f.close()
        common.new_captcha()
    else:
        content = 'invalid captcha'
    return '200 ', header, content
    
