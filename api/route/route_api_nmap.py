# -*- coding: utf-8 -*-
"""
Created on 2/21/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
from threading import Thread
from urllib import request
from flask import Blueprint, request, jsonify, Response
from api.service.scan_single_ip import ScanSingleIp
from time import sleep

nmap_api = Blueprint('api', __name__, url_prefix='/api')


@nmap_api.route('/', methods=['GET'])
def index_b4rt():
    return 'b4rt'


@nmap_api.route('/', methods=['POST'])
def index_post():
    return 'b4rt2'


@nmap_api.route("/scan_single_ip/", methods=['POST'])
def launch_scan():
    data = request.get_json()
    ip = data['ip']
    scan_single_ip = ScanSingleIp(ip=ip)
    response_scan = scan_single_ip.launch_scan()

    return jsonify(response_scan)
