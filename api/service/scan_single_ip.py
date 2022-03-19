# -*- coding: utf-8 -*-
"""
Created on 2/27/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
import os
import subprocess as sp, shlex
import xmltodict
import json
from api.service.utils.logger import error_logger, info_logger


class ScanSingleIp:
    def __init__(self, ip, port=None, timeout=None, threads=None, verbose=None, output=None, output_file=None,
                 output_json=None, command=None, output_file_xml=None):
        self.nmap_command = None
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.threads = threads
        self.verbose = verbose
        self.output_name = "output_files/scan_" + self.ip
        self.output_xml = output_file_xml
        self.output_file = output_file
        self.output_json = output_json

        self.command = command

    def initial_scan(self):
        self.nmap_command = "nmap -sS -T4 -Pn " + self.ip + " -oA " + self.output_name
        output = sp.Popen(self.nmap_command, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)

        print(output)
        output.wait()
        with open(self.output_name + '.xml', 'r') as file:
            self.output_xml = file.read()
        self.upload_files_s3()
        self.xml_to_json()
        return json.dumps(self.parse_json_output())

    def xml_to_json(self):
        self.output_json = xmltodict.parse(self.output_xml)
        print(self.output_json)

    def parse_json_output(self):
        host = self.output_json['nmaprun']['host']
        ports = host['ports']['port']
        return ports

    def upload_files_s3(self):
        try:
            os.remove(self.output_name + '.xml')
            os.remove(self.output_name + '.nmap')
            os.remove(self.output_name + '.gnmap')
        except OSError as e:
            error_logger.error(e)
