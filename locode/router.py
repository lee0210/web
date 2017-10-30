from urllib.parse import parse_qs
import common
import importlib
import re
import logging
import cgi

routing_rules = {}
middlewares = {}

class rule_builder:
    @staticmethod
    def __resolve_handler(handler):
        return re.match('(^\w[\w\.]+)@(\w+)', handler).groups()

    def get(self, url, handler):
        module, method = rule_builder.__resolve_handler(handler)
        self._rule = {
            'method': 'get',
            'url': url,
            'handler': getattr(importlib.import_module(module), method)
        }
        return self

    def post(self, url, handler):
        module, method = rule_builder.__resolve_handler(handler)
        self._rule = {
            'method': 'post',
            'url': url,
            'handler': getattr(importlib.import_module(module), method)
        }
        return self

    def middleware(self, name, handler):
        module, method = rule_builder.__resolve_handler(handler)
        self._middleware = {
            'name': name,
            'handler': getattr(importlib.import_module(module), method)
        }
        return self

    def before_process(self, middleware_list):
        self._rule['before'] = middleware_list
        return self

    def after_process(self, middleware_list):
        self._rule['after'] = middleware_list
        return self

    def register(self):
        if hasattr(self, '_rule'):
            global routing_rules
            routing_rules[self._rule['url']] = self._rule
        if hasattr(self, '_middleware'):
            global middlewares
            middlewares[self._middleware['name']] = self._middleware

def get(url, handler):
    return rule_builder().get(url, handler)

def post(url, handler):
    return rule_builder().post(url, handler)

def middleware(name, handler):
    return rule_builder().middleware(name, handler)
#
# @param locode.request.request
#
# @return locode.response.response 
#
def handle(e):
    rule = routing_rules[e['PATH_INFO']]
    after = rule.get('after', [])
    before = rule.get('before', [])
    for m in before:
        if not middlewares.get(m).get('handler')(e):
            return 
    if not rule.get('handler')(e):
        return
    for m in after:
        if not middlewares.get(m).get('handler')(e):
            return 

def before(e):
    e['L_QUERY_STRING'] = parse_qs(e['QUERY_STRING'])
    e['L_FORM_DATA'] = cgi.FieldStorage(fp=e['wsgi.input'], environ=e)
    e['L_HTTP_STATUS'] = '200 '
    e['L_HTTP_HEADER'] = common.http_header
    e['L_HTTP_CONTENT'] = ''
    return

def after(e):
    return
