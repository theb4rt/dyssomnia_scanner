# -*- coding: utf-8 -*-
"""
Created on 2/15/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
from .route_api_nmap import nmap_api
from config import app


app.register_blueprint(blueprint=route_api_nmap.nmap_api)
