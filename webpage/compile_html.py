#!/usr/bin/python

import re
import sys

base = '/workspace/web/webpage'

def load_file(path):
    try:
        f = open(path, 'r')
        return f.read()
    except Exception, e:
        return None
    finally:
        if(locals().has_key('f')): f.close()

def get_parent(data):
    extend = re.findall("@extend\(\s*\'(\w+?)\'\s*\)", data)
    return None if extend == [] else extend[0]

def extract(data):
    fills = re.findall("@fill\(\s*'(\w+)'\s*,\s*\'([\w\W]+?)\'\)", data)
    rt = { fill[0] : fill[1] for fill in fills }
    fills = re.findall("@fill\(\s*'(\w+)'\s*\)([\w\W]+?)@endfill", data)
    rt.update({ fill[0] : fill[1] for fill in fills })
    return rt

def compile(path):
    path ='%s/%s.template.html'%(base, path)
    data = load_file(path)
    parent = get_parent(data)
    if(parent is None):
        return data
    p_data = compile(parent)
    data = extract(data)
    return p_data.format(**data)

def save_file(path, content):
    try:
        f = open(path, 'w+')
        f.write(content)
    finally:
        if(locals().has_key('f')): f.close()

if __name__ == '__main__':
    output = '/data/html/%s.html'%sys.argv[1]
    compiled = compile(sys.argv[1])
    save_file(output, compiled)
    print 'compile %s completed... output: %s'%(sys.argv[1], output)
 
    

    
