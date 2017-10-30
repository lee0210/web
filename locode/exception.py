def default(e):
    e['L_HTTP_STATUS'] = '502 '
    e['L_HTTP_HEADER'] = {}
    e['L_HTTP_CONTENT'] = 'Opss! Service Unavailable'
    return
