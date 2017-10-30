import common
import hashlib
import base64
import json
import logging

def get(e):
    e['L_HTTP_CONTENT'] = 'This is user.get function'
    return

def test(e):
    common.set_redirect_header(e, 'http://120.24.174.183/index')
    return

def post(e):
    e['L_HTTP_CONTENT'] = 'This is user.post function'
    return

def postjson(e):
    form = e['L_FORM_DATA']
    logging.debug(json.loads(form.value))
    e['L_HTTP_CONTENT'] = 'This is user.post function'
    return

def event(e):
    key = e.get('HTTP_SEC_WEBSOCKET_KEY') + common.wsk
    logging.debug(key)
    key = hashlib.sha1(key.encode('utf8')).digest()
    logging.debug(key)
    key = base64.b64encode(key).decode('utf8')
    logging.debug(key)
    e['L_HTTP_STATUS'] = '101 '
    e['L_HTTP_HEADER'] = common.websocket_header(key)
    e['L_HTTP_CONTENT'] = ''


