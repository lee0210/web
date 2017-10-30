import common
import cgi
import re
import uuid
import conf

class html_editor(common.html_base):
    rf_base = ['title', 'header_attrs', 'body']
    rf_body = ['nav_bar', 'content']
    tp_base = conf.root + '/webpage/base.html'
    tp_nav_bar = conf.root + '/webpage/nav_bar.html'
    tp_body = conf.root + '/webpage/blog_body.html' 

css = """<style>
div .lee_seperator{
    height: 1px;
    margin: 9px 0;
    overflow: hidden;
    background-color: #e5e5e5;
}
</style>
"""

header_attrs = ["""<script src="/editor.js"></script>""", css]
editor = html_editor()
editor.title = 'Blog'
editor.header_attrs = '\n'.join(header_attrs)

def process(e, r):
    header = common.default_text_header()
    form = cgi.FieldStorage(fp=e['wsgi.input'], environ=e)
    # validation
    inputs = ['url', 'content', 'captcha']
    if not len(inputs) == sum([x in inputs for x in form]):
        response = 'invalid request'
        return '200 ', header, response
    if not common.check_captcha(form['captcha'].value):
        response = 'invalid captcha'
        return '200 ', header, response
    url = form['url'].value
    pattern = '^:(new|delete|update)\/\/(\w*)'
    request = re.findall(pattern, url)
    if [] == request:
        response = 'invalid request'
        return '200 ', header, response
    option, url = request[0] 
    if option == 'new':
        if url == '':
            url = uuid.uuid1().hex
    if option in ['new', 'update']:
        editor.content = form['content'].value
        content = editor.get_result('tp_base')
        common.create_static_html(url, content) 
    if option == 'delete':
        common.delete_static_html(url)
    common.new_captcha()
    response = url
    return '200 ', header, response
 
