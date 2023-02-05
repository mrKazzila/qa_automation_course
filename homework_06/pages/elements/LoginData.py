from random import randint


class Admin:
    LOGIN: str = 'user'
    PASSWORD: str = 'bitnami'


class User:
    FIRST_NAME: str = 'Rick'
    LAST_NAME: str = 'Astley'
    EMAIL: str = f'NeverGonnaGiveYouUp{randint(0, 1000000)}@mail.com'
    PHONE: str = '+91112345678'
    LOGIN: str = 'PASSWORD'
    PASSWORD: str = 'LOGIN'
