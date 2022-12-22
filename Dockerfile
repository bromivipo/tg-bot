FROM python:3.10

WORKDIR /usr/share/bot
COPY . .

RUN pip install aiogram==2.23.1

CMD ["python", "./main.py"]

