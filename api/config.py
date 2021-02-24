import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = os.environ.get('MONGO_URI') + os.path.join(basedir, 'app.db')
    PORT = int(os.environ.get('PORT') or 5000)
    IP = os.environ.get('IP') or '0.0.0.0'