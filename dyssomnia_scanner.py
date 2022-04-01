# -*- coding: utf-8 -*-
"""
Created on 2/15/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
from flask import Flask

app = Flask(__name__)

import api_nmap
import config


if __name__ == '__main__':
    app.run()