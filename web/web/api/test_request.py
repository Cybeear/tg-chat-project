import requests
from rest_framework.response import Response



def post_user():
    """добавление юзверя"""
    url = 'http://127.0.0.1:8000/api/user'
    data = {'username': 'qwe', 'first_name': '', 'last_name': '', 'user_id_tg': '1313', 'warn': '0'}
    send = requests.post(url=url, json=data)
    return send


def post_faq():
    """добавление справки"""
    url = 'http://127.0.0.1:8000/api/faq'
    data = {'title': 'test', 'description': 'test test'}
    send = requests.post(url=url, json=data)
    return send


def post_poll():
    """добавление голосования"""
    url = 'http://127.0.0.1:8000/api/poll'
    data = {'keyboard_id': '123', 'user_id': '112233'}
    send = requests.post(url=url, json=data)
    return send


def post_block():
    url = 'http://127.0.0.1:8000/api/block'
    data = {'user': '300', 'permanent': False}
    send = requests.post(url=url, json=data)
    print(send)
    print(Response)
    return send

#post_user()
#post_faq()
#post_poll()
post_block()