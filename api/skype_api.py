# -*- coding: utf-8 -*-
from skypebonds import app

__author__ = 'Vladimir'


@app.route('/')
def hello_world():
    return 'Hello World!'
