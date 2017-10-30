import db
import random
import common
import os

def process(e, r):
    header = common.default_text_header()
    captcha = db.captcha.get_lock()
    captcha.id = u'main'
    if not captcha.chain():
        captcha.count = 0
        captcha.code = ('000000' + str(random.randint(0,999999)))[-6:]
        captcha.write()
        captcha.chain()
    if captcha.count < 3:
        captcha.count = captcha.count + 1
        captcha.update()
        os.system('echo "{0}" | mailx -s "CAPTCHA" jw@qubitlee.com'.format(captcha.code))
    else:
        print 'unlock'
        captcha.unlock()
    content = 'success'
    return '200 ', header, content
    
