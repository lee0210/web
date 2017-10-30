import os
import logging
import sys
import traceback
import config
from locode import router
from locode import exception

def application(e, r):
    try:
        logging.debug(e)
        router.before(e)
        router.handle(e)
        router.after(e)
    except Exception as err:
        logging.error(err)
        traceback.print_exc()
        exception.default(e)
    r(e.get('L_HTTP_STATUS'), list(e.get('L_HTTP_HEADER').items()))
    return [e.get('L_HTTP_CONTENT').encode(config.encoding)]

logging.basicConfig(level=logging.DEBUG)
