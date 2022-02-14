# Карточная игра для телеграм.

Суть игры описывает игра БлекДжек.

Когда пользователь последовательно набирает случайные карты из колоды и набирает балы не более 21. 

Для телегам бота есть несколько библиотек.

python-telegram-bot - имеет несколько сложноватый синтаксис поэтому будем использовать pytelegramapi 
      
Установим библиотеку.

    pip install telegrambotapi

Регистрируем бота.

Заходим в клиенте на BotFather и набираем имя и логин бота.



Создание бота.

    import telebot
    bot = telebot.TeleBot(key)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

    bot.polling()

Выбираем случайные карты и считаем очки.

    from os import listdir
    from os.path import isfile, join
    import random

    def get_score(cards):
        score = 0
        for card in cards:
            num = int(card.split('-')[0])
            score += num
        return score

    def get_random_cards():
        path = 'images'
        out = []
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        for i in range(1,4):
            rand = random.randint(0,len(onlyfiles)-1)
            out.append(onlyfiles[rand])
            onlyfiles.pop(rand)
        return out

Посылаем картинки и сколько набрали.

    cards = get_random_cards()
    score = get_score(cards)
    bot.send_message(message.chat.id, 'Вы набрали: %s!' % score)
    for card in cards:
        bot.send_photo(chat_id=room_id, photo=open('images/%s' % card, 'rb'))

Делаем функцию для склеивания 3-х картинок в одну.

Устанавливаем инструмент

    pip install Pillow

Определяем функцию

    from PIL import Image
    def combine_images(cards,name):
        images = []
        for image in cards:
            images.append(Image.open('images/%s' % image))
        new_im = Image.new('RGB', (210, 107))
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset += 70
    new_im.save(name)

Используем.

    combine_images(cards,'player.png')
    bot.send_photo(chat_id=room_id, photo=open('player.png', 'rb'))

Посылаем 3 кнопки.


    from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Вскрыться',callback_data='one'))
    markup.add(InlineKeyboardButton('Дать дальше',callback_data='two'))
    markup.add(InlineKeyboardButton('Упасть',callback_data='tree'))

    ...

    bot.send_message(message.chat.id, 'Вы набрали: %s!' % score, reply_markup=markup)


Делаем обработчики.

    @bot.callback_query_handler(lambda first: first.data=="one")
    def button_send(query):
        bot.send_message(query.message.chat.id, 'Вы вскрылись!')

    @bot.callback_query_handler(lambda first: first.data=="two")
    def button_send(query):
        bot.send_message(query.message.chat.id, 'Вы дали дальше!')

    @bot.callback_query_handler(lambda first: first.data=="tree")
    def button_send(query):
        bot.send_message(query.message.chat.id, 'Вы упали!')

