# -*- coding: utf-8 -*-
"""
Created on 3/22/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
import os
from dotenv import load_dotenv

from dyssomnia_scanner import app

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# PostgreSQL
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
    DB_USER=os.getenv("DB_USER", 'postgres'),
    DB_PASS=os.getenv("DB_PASSWORD", '1234'),
    DB_ADDR=os.getenv("DB_ADDRESS", '127.0.0.1'),
    DB_NAME=os.getenv("DB_NAME", 'postgres'))

DATABASE_CONNECT_OPTIONS = {}

# Threads
THREADS_PER_PAGE = 2

# CSRF PROTECTION
CSRF_ENABLED = True

# CSRF KEimport dyssomnia_scanner.configY
CSRF_SESSION_KEY = "secret"

# SECRET KEY
SECRET_KEY = "secret"

config = {
    'app': {
        'APP_NAME': os.getenv('FLASK_APP', 'dyssomnia_scanner'),
        'APP_VERSION': os.getenv('APP_VERSION', '1.0.0'),
        'SECRET_KEY': os.getenv('APP_SECRET_KEY', None),
        'TIMEZONE': os.getenv('APP_TIMEZONE', 'UTC'),
    },
    'db': {
        'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    },
}

app.config.update(**config.get('app'))
app.config.update(**config.get('db'))
