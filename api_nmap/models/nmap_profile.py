"""
Created on 4/1/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
from api_nmap.database import db


class NmapProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_name = db.Column(db.String(80), allow_null=False)
    ip = db.Column(db.String(64), allow_null=False)


