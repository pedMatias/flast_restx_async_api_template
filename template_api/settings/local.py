from .base import *

HOST = 'localhost'
PORT = 5000
DEBUG = True

REDIS = {
    'host': '127.0.0.1',
    'port': 6379}

DB_MYSQL = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'mysql',
    'name': 'app_tagger'}
DB_URI = 'mysql://{username}:{password}@{server}/{db_name}'.format(
    username=DB_MYSQL['user'],
    password=DB_MYSQL['password'],
    server=DB_MYSQL['host'],
    db_name=DB_MYSQL['name']
)
