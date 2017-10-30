from locode import dba
from locode import cypher
from common import set_redirect_header
from common import set_json_header
from urllib.parse import parse_qs 
from http.cookies import SimpleCookie
import logging
import random
import cgi
import locode
import json

def check_auth(e):
    if auth(e, False, False): 
        e['L_HTTP_CONTENT'] = json.dumps({'rt': '0'})
    else:
        e['L_HTTP_CONTENT'] = json.dumps({'rt': '1'})
    set_json_header(e)
    return

def auth(e, change_token=True, redirect=True):
    cookie = SimpleCookie(e.get('HTTP_COOKIE')).get('data')
    if cookie is not None:
        cookie = cookie.value
        logging.debug(cookie)
        cookie, user = cypher.decrypt(cookie)
        logging.debug(cookie)
        logging.debug(user)
        if cookie.get('user') == user:
            if change_token:
                sc = SimpleCookie()
                sc['data'] = cypher.encrypt(cookie, user)
                e['L_HTTP_HEADER']['Set-Cookie'] = sc.output(header='', sep=';')
            return True
    if redirect:
        set_redirect_header(e, '/login')
    return False

def login(e):
    form = e.get('L_FORM_DATA')
    code = form.getvalue('captcha')
    user = form.getvalue('user')
    rt = dba.sql().table('captcha').read({'id': user})
    logging.debug(rt)
    logging.debug(code)
    e['L_HTTP_STATUS'] = '200 '
    set_json_header(e)
    if not locode.is_empty(rt) and rt[0].get('code') == code:
        e['L_HTTP_CONTENT'] = json.dumps({'rt': '0'})
        cookie = {}
        cookie['user'] = user
        sc = SimpleCookie()
        sc['data'] = cypher.encrypt(cookie, user)
        e['L_HTTP_HEADER']['Set-Cookie'] = sc.output(header='', sep=';')
        dba.sql().table('captcha').update({'code': ('000000' + str(random.randint(0,999999)))[-6:]}, {'id': user})
        return
    e['L_HTTP_CONTENT'] = json.dumps({'rt': '1'})
    return
        
    
    
