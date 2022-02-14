# Модель. Админка.
 
Устанавливаем python3-venv  

    sudo apt-get install python3-venv

Создаем виртуальное окружение и активируем его.

    python3 -m venv venv
    . ./venv/bin/activate

Создаем файл requirements.txt с зависимостями.

    Django==3.0.6
    telethon==1.14.0

Устанавливаем зависимости.

    pip install -r requirements.txt

Создаем проект.

    django-admin startproject telegram_poster

Запускаем миграцию и создаем приложение.

    ./manage.py migrate
    ./manage.py startapp main

Включаем приложение в settings.py в INSTALLED_APPS.

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'main'
    ]

Создаем модель.



    from django.db import models

    class Client(models.Model):
        name = models.CharField(max_length=250, db_index=True)
        secret = models.CharField(max_length=250, db_index=True)

    class TelegramUser(models.Model):
        key = models.CharField(max_length=250, db_index=True)
        client = models.ForeignKey(Client, on_delete=models.CASCADE)

Создаем и применяем миграцию.

    ./manage.py makemigrations main
    ./manage.py migrate


Создаем админ интерфейс.


    from django.contrib import admin
    from main.models import Client, TelegramUser

    @admin.register(Client)
    class ClientAdmin(admin.ModelAdmin):
        list_display = ['name', 'secret']

    @admin.register(TelegramUser)
    class TelegramUserAdmin(admin.ModelAdmin):
        list_display = ['key', 'client']

Получаем секретный ключ приложения телеграм.

[ссылка для входа](https://my.telegram.org/)

![start page]({path-to-subject}/images/1.png)

Делаем команду заполнения таблицы Client main/management/commands/load_data.py.

    from django.core.management.base import BaseCommand, CommandError
    from main.models import Client


    class Command(BaseCommand):

        def handle(self, *args, **options):
            Client.objects.all().delete()
            print('Load client')
            c = Client()
            c.name = 'wezom'
            c.secret = '123'
            c.save()


Делаем команду регистрации.


    from django.core.management.base import BaseCommand, CommandError
    from telethon import TelegramClient, events
    from telegram_poster.settings import TELEGRAM_ID, TELEGRAM_KEY, TELEGRAM_SESSION_NAME
    import asyncio
    from asgiref.sync import sync_to_async, async_to_sync

    client = TelegramClient(TELEGRAM_SESSION_NAME,TELEGRAM_ID,TELEGRAM_KEY)

    from main.models import Client, TelegramUser

    @sync_to_async
    def register(message,from_id):
        message = message.lower()
        try:
            c = Client.objects.get(name=message)
            try:
                user = TelegramUser.objects.get(key=from_id)
                message = 'Вы уже зарегистрированы.'
            except:
                u = TelegramUser()
                u.key = from_id
                u.client = c
                u.save()
                message = 'Вы были зарегистрированы.'
        except Exception as e:
            print(e)
            message =  'Запрашиваемый клиент не найден. %s' % e
        return message

    @client.on(events.NewMessage())
    async def normal_handler(event):
        message = event.message.to_dict()
        print(message['message'])
        message = await register(message['message'], message['from_id'])
        await client.send_message(904392408, message)

    class Command(BaseCommand):

        def handle(self, *args, **options):
            print('Run registrator')
            client.start()
            client.run_until_disconnected()


Добавляем папку с шаблонами.

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],


Делаем вьюху для отправки уведомления.


## Устанавливаем celery

    celery
    redis==3.2.0

Обязательно указываем версию для redis.

Редактируем настройки.

    BROKER_URL = 'redis://localhost:6379' 

Создаем приложение селери в celery.py.

    import os  
    from celery import Celery
    from django.conf import settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_poster.settings')
    app = Celery('telegram_poster')  
    app.config_from_object('django.conf:settings')  
    app.autodiscover_tasks(settings.INSTALLED_APPS) 

Создаем таску tasks.py.

    from telegram_poster.celery import app
    from celery import shared_task 
    from telegram_poster.settings import TELEGRAM_ID, TELEGRAM_KEY, TELEGRAM_SESSION_NAME
    import asyncio
    from telethon import TelegramClient
    from django import db


    async def send(phone,client,message):
        print('Send test ')
        await client.connect()
        await client.send_message(phone, message) 
        await client.disconnect()


    @shared_task
    def send_message(phone,message):
        print('Sending message')
        db.connections.close_all()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient(TELEGRAM_SESSION_NAME,TELEGRAM_ID,TELEGRAM_KEY,loop=loop)
        loop.run_until_complete(send(phone,client,message))


Вызываем таск из вьюхи.

    from django.shortcuts import render
    from .models import Client, TelegramUser
    from telegram_poster.tasks import send_message
    from django.views.decorators.csrf import csrf_exempt

    def index(request):
        return render(request,'index.html')

    @csrf_exempt
    def notify(request):

        try:
            c = Client.objects.get(secret=request.POST['secret'])
            for user in TelegramUser.objects.filter(client=c):
                message = request.POST['message']+' Источник: '+c.name
                send_message.delay(user.key,message)
        except:
            pass
        return render(request,'index.html')

Запуск вокера селери.

    celery worker -A telegram_poster

![admin]({path-to-subject}/images/1.png)    
