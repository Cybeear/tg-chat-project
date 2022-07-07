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


def get_warn(user_id) -> dict:
    url = config.WEB_URL + f"api/block/{user_id}?format=json"
    warn = requests.get(url=url)
    return warn.json()


def mute_time(user_id):
    warn = get_warn(user_id=user_id)["warn"]
    _time = time() + warn * 600 + (warn - 1) * 600
    return abs(_time)


def get_faq() -> list:
    url = config.WEB_URL + "api/faq?format=json"
    response = requests.get(url=url)
    content = response.json()
    return content


def push_user(user) -> bool:
    """
    Функция добавляет в web нового telegram-пользователя
    TODO проверять, что пользователь уже есть (отдельной функцией?)
    TODO проверять, что добавляется именно пользователь, а не бот
    TODO возвращается bool, который нигде не проверяется
    """
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


#Функция отправки благодарности на сервер django для записи в БД
def send_pet(user_id):
    pass
