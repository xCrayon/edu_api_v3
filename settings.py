#!/usr/bin/python3
# coding: utf-8
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.join(PROJECT_DIR, 'mainapp')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
USER_DIR = os.path.join(STATIC_DIR, 'user')


class Dev():
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@ip/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True


if __name__ == '__main__':
    print(PROJECT_DIR)
    print(BASE_DIR)
