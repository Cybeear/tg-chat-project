from aiogram.types.user import User
from typing import Union
from time import time
import requests

from config import config


# TODO Надо переписать модуль полностью, сделать функции рабочими(пока только прототипы), сделать функции с post запросами

def get_token() -> str:
    """
    Функция возвращает токен из web'a по связке логин + пароль (изначально надо зайти в админку и создать там юзера для Бота).
    В ответ на запрос придет словарь, содержащий имя бота и токен, который
    нужно использовать при запросах на другие методы api. Слеш в конце адреса обязателен!!!
    """
    data = {'username': config.LOGIN_USERNAME, 'password': config.LOGIN_PASSWORD}
    url = f'{config.WEB_URL}api/login/'
    response = requests.post(url=url, data=data)
    return response.json()["token"]


def get_warn(user_id: Union[str, int]) -> int:
    """
    Функция возвращает кол-во предупреждений по id пользователя в телеграм,
    если такой пользователь есть в БД (иначе будет error)!
    """
    url = f"{config.WEB_URL}api/block"
    data = {'user': user_id, 'permanent': False}
    headers = {"Authorization": f"Bearer {get_token()}"}
    response = requests.post(url=url, data=data, headers=headers)
    return response.json()["warn"]


def mute_time(user_id: Union[str, int]) -> float:
    """
    Функция вычисляет время блокировки пользователя на основе кол-ва предупреждений
    """
    warn = get_warn(user_id=user_id)
    _time = time() + warn * 600 + (warn - 1) * 600
    return abs(_time)


def get_faq() -> list:
    """
    Функция возвращает faq из web'a.
    TODO в ответе может не быть нужной структуры, если предварительно не вызван post-метод api/faq
    """
    url = f'{config.WEB_URL}api/faq?format=json'
    headers = {"Authorization": f"Bearer {get_token()}"}
    response = requests.get(url=url, headers=headers)
    content = response.json()
    return content


def push_user(user: User) -> bool:
    """
    Функция добавляет в web нового telegram-пользователя
    TODO проверять, что пользователь уже есть (отдельной функцией?)
    TODO протестировать функцию (нельзя без удаления созданных пользователей)
    TODO возвращается bool, который нигде не проверяется
    """
    if user.is_bot:
        return False
    url = f'{config.WEB_URL}api/user'
    headers = {"Authorization": f"Bearer {get_token()}"}
    data = {
            "user_id_tg": f"{user.id}",
            "first_name": f"{user.first_name}",
            "last_name": f"{user.full_name}",
            "username": f"{user.mention}"
           }
    response = requests.post(url=url, data=data, headers=headers)
    return True if 'warn' in response.json() else False


def add_vote(user: User, keyboard_id: Union[str, int]) -> dict:
    """
    Запрос POST на добавление голосования. Отправляем id клавиатуры и id кто проголосовал.
    В ответ придет id голосования, кто проголосовал и общее количество голосовавших. Повторы не будут учитываться
    """
    url = f'{config.WEB_URL}/api/poll'
    headers = {"Authorization": f"Bearer {get_token()}"}
    data = {'keyboard_id': '123', 'user_id': '112233'}
    response = requests.post(url=url, data=data, headers=headers)
    return response.json()


#Функция отправки благодарности на сервер django для записи в БД
def send_pet(user_id):
    pass
