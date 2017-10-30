import common
import urlparse
import hashlib

appid = 'wxd3bfd26697828025'
appsecret = 'a7e7ae4e6a7cb469af7208ceeea5b78b'

def process(e, r):
    header = common.default_text_header()
    valid_signature, queries = check_signature(e, r)
    if not valid_signature:
        return '200 ', header, 'invalid request'
    return '200 ', header, queries['echostr'][0]


def check_signature(e, r):
    queries = urlparse.parse_qs(e['QUERY_STRING'])
    keys = ['signature', 'timestamp', 'nonce', 'echostr']
    if len(keys) != sum([x in keys for x in queries]):
        return False, None
    string_array = queries['timestamp'] + queries['nonce'] + ['qubitlee']
    string_array.sort()
    signature = hashlib.sha1(''.join(string_array)).hexdigest()
    if signature != queries['signature'][0]:
        return False, None
    return True, queries
