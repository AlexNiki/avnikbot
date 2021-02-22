import os

TOKEN = '1661150170:AAFxO9tIQlwpSB0QgJzgkHjQjBUP_jiylEM'

bd_array = [
            ["Никифорова", "Ева", "Александровна", "22.06.2017"],
            ["Никифорова", "Алена", "Алмазовна", "02.01.1989"],
            ["Капарова", "Наташа", "Алмазовна", "29.08.1986"]
           ]

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/bd-alexniki-bot'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']