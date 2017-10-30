from datetime import datetime
from datetime import timedelta

GMT_format = "%a, %d %b %Y %H:%M:%S GMT"

wsk = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

http_header = {
    'Host': '120.24.174.183',
    'Content-Type': 'text/html; charset=utf-8',
}   

def set_json_header(e):
    e['L_HTTP_HEADER']['Content-Type'] = 'application/json; charset=utf-8'

def set_redirect_header(e, url):
    e['L_HTTP_STATUS'] = '307 '
    e['L_HTTP_HEADER']['Location'] = url
 
def websocket_header(key, protocol = None):
    header = dict(http_header)
    header.pop('Content-Type')
    header['Upgrade'] = 'websocket'
    header['Connection'] = 'Upgrade'
    header['Sec-WebSocket-Accept'] = key
    if protocol is not None:
        header['Sec-WebSocket-Protocol'] = protocol
    return header
