import os

TOKEN = '1661150170:AAFxO9tIQlwpSB0QgJzgkHjQjBUP_jiylEM'

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/bd-alexniki-bot'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']