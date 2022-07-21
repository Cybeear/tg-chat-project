FROM python:3.10-buster

WORKDIR /usr/src/app/tg-bot

COPY requirements.txt /usr/src/app/tg-bot

RUN python -m pip install --upgrade pip; \
    pip install -r /usr/src/app/tg-bot/requirements.txt

COPY . /usr/src/app/tg-bot

CMD python main.py $MODE
