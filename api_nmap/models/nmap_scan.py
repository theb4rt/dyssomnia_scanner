"""
Created on 4/1/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
from api_nmap.database import db


class NmapScan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nmap_profile= db.Column(db.Integer, db.ForeignKey('nmap_profile.id'))
    scan_result = db.Column(db.JSON,  )
    scan_protocol = db.Column(db.String(4),nullable=True)
    open_ports_tcp= db.Column(db.JSON, nullable=True)
    open_ports_udp= db.Column(db.JSON, nullable=True)
    scan_arguments = db.Column(db.JSON, nullable=True)


