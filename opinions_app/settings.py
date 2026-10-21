
import os


class Config(object):

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                        'sqlite:///opinions.db')
    SECRET_KEY = os.getenv('SECRET_KEY')
