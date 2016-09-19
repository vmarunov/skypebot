# -*- coding: utf-8 -*-
"""
Skype bot
"""
from flask import Flask


__author__ = 'Vladimir'


app = Flask(__name__)

from api.skype_api import *

if __name__ == '__main__':
    context = ('/home/vmarunov/skypebonds/star.skybonds.net.crt',
               '/home/vmarunov/skypebonds/star.skybonds.net.key')
    # app.run(host='0.0.0.0', port=5003, threaded=True, debug=True)
    app.run(host='0.0.0.0', port=5003, ssl_context=context, threaded=True,
            debug=True)
