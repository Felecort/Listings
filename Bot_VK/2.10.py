
# VERSION 2.9

# Импорт модулей
from social_ethosa import *
from SimpleQIWI import *

import datetime
import re
import time
import os

# Присваивание значений переменным
rmode = 0
msglist = admins = []
autotr = log_flug = False
trlang = 'en'
counter = 1

# Создание глобальных переменных
def glbs():
    global peer_id
    global message_id
    global trlang
    global chat
    global chat_msg

# Чтение необходимой информации
with open('options.py', "r",encoding="utf-8") as f:
    exec(f.read())
    f.close()

# Создание файла для логов
today = datetime.datetime.today()
date = today.strftime("%Y-%m-%d  %H-%M-%S")
if not os.path.exists('Logs_Bot'): os.makedirs('Logs_Bot')
file_path = os.path.join('Logs_Bot',"log " + date + ".log")

# Запись дефолтной информации в лог
log_file = open(file_path, "w")
log_file.write ("Бот запущен:  " + str(date) + "\nПользователь: " + acc_id + "\n---------------------------------\nЛоги команд:\n\n")
log_file.close()

print(date)
print('Запуск бота')

# Логирование команд и ошибок
def Log(counter, message):
    log_file = open(file_path, "a")
    log_file.write(counter + message + "\n\n\n")
    log_file.close()

""" Основные функции """

# Бан страницы
def ban(id):
    vk.account.ban(owner_id=id)

# Разбан страницы
def unban(id):
    vk.account.unban(owner_id=id)

# Отправка заявки в друзья
def addfriend(id):
    vk.friends.add(user_id=id)

# Удаление из друзей
def delfriend(id):
    vk.friends.delete(user_id=id)

# Отправка фото
def image(path,**kwargs):
    photo = vk.uploader.uploadMessagePhoto(files=path, peer_id=peer_id, formatting=True)
    vk.messages.send(attachment=",".join(photo),peer_id=peer_id,**kwargs)

# Отправка сообщения (Python кода)
def send(msge,**kwargs):
    vk.messages.send(message=msge,peer_id=peer_id,**kwargs)

# Отправка стикера
def s(stik):
    vk.messages.send(sticker_id=stik,peer_id=peer_id)

# Добавление(возврат) пользователя в беседу
def add(id):
    vk.messages.addChatUser(chat_id=int(peer_id)-2000000000,user_id=id)

# Удаление пользователя из беседы (если есть или вышел)
def back(id):
    try: vk.messages.removeChatUser(user_id=id,chat_id=int(peer_id)-2000000000)
    except: 'error'
    vk.messages.addChatUser(chat_id=int(peer_id)-2000000000,user_id=id)

# Кик пользователя
def kick(id):
    vk.messages.removeChatUser(user_id=id,chat_id=int(peer_id)-2000000000)

# Получение ID
def id(idr):
    idr = idr.replace('https://vk.com/','')
    if not str(idr).isdigit():
        domens = re.findall(r"(?:@|\[|id)([^\[\@\|\]\s,\(\)]+)", idr)
        ids = vk.users.get(user_ids=",".join(domens))
        ids = [i["id"] for i in ids["response"]]
        return ids[0]
    else: return idr

# Получение сообщения
def rmsg():
    if chat: chat_msg = vk.messages.getById(message_ids=message_id)
    return [chat_msg['response']['items'][0]['reply_message']['text'],chat_msg['response']['items'][0]['reply_message']['id']]

# Удаление сообщения
def delete(message_id1):
    vk.messages.delete(delete_for_all=1,message_ids=message_id1)

""" Почти бесполезные функции """

# Отчёт(Как бы нужно, но нет)
def msend(error):
    if err_id != 0: vk.messages.send(message=error,peer_id=err_id)

# Редактирование сообщения
def edit(msg,**kwargs):
    vk.messages.edit(**kwargs,peer_id=peer_id,message=msg,message_id=message_id,keep_forward_messages=1)

# Перевод на русский
def ru(msg):
    return yt.translate(text=msg, lang="ru")['text'][0]

# Перевод на английский
def tr(msg):
    return yt.translate(text=msg, lang=trlang)['text'][0]

# Основной цикл
for event in vk.longpoll.listen():
    try:
        if event['type'] == 4:
            peer_id = event['peer_id']
            message = event['text'].replace('<br>','\n').replace('°',' ').replace('&lt;','<').replace('&gt;','>').replace('&quot;','"')
            message_id = event['message_id']
            reply = 0

            # Получение id пользователя, на сообщение которого ответили
            if 'mentions' in event['object']: reply = event['object']['mentions'][0]
            if 'from' in event['object']:

                # Беседа
                from_id = event['object']['from']
                chat = True
            else:

                # Личные сообщения
                chat = False
                chat_msg = vk.messages.getById(message_ids=event['message_id'])
                from_id = chat_msg['response']['items'][0]['from_id']
                reply = peer_id

            # Права администратора(владельца бота )
            admin = False
            if str(from_id) == acc_id: admin = True
            elif from_id in admins: admin = True

            # Модуль удаления записанных сообщений
            if rmode == 1 and admin: msglist.append(int(event['message_id']))

            # Обработка команд
            if admin:

                # Разделение
                log_flug = True
                cmd = message.split(' ',maxsplit=1)

                if message[:2] == '//': exec(message[2:])

                elif cmd[0] in ['/kick','/кик']:
                    if len(cmd) == 1: kick(reply)
                    else: kick(id(cmd[1]))

                elif cmd[0] in ['/rt','==']:
                    if len(cmd) > 1: edit(ru(cmd[1]))
                    else: edit(ru(rmsg()[0]))

                elif cmd[0] in ['/t','~~']:
                    if len(cmd) > 1: edit(tr(cmd[1]))
                    else: edit(tr(rmsg()[0]))

                elif cmd[0] in ['/return','/back','.вернуть,', '/вернуть']:
                    if len(cmd) == 1: back(reply)
                    else: back(id(cmd[1]))

                elif message in ['/start','/старт']:
                    rmode = 1
                    msglist = [int(event['message_id'])]

                elif cmd[0] in ['/lang','/язык']:
                    if len(cmd)>1: trlang = cmd[1]
                    else: trlang = 'en'

                elif message in ['/stop','/стоп']:rmode = 0

                elif message in ['/delete','/удалить','/del']:
                    msglist.append(int(event['message_id']))
                    vk.messages.delete(delete_for_all=1,message_ids=str(str(msglist).replace('[','').replace(']','')))
                    msglist=[]
                    rmode = 0

                elif message in ['/del message','##', '/удалить сообщ']:
                    try: delete(rmsg()[1])
                    except: 'err'
                    delete(message_id)

                elif message in ['/i','~']:
                    try: edit(BotWrapper().translit(rmsg()[0]))
                    except: 'err'

                elif message in ['/a','*','/trOn']:
                    autotr = True
                    delete(message_id)

                elif message in ['/aa','**','/trOff']:
                    autotr = False
                    delete(message_id)

                elif cmd[0] in ['/in','/лс']:
                    if len(cmd) > 1: vk.messages.send(message=cmd[1],peer_id=str(reply))
                    else: vk.messages.send(message='.',peer_id=str(reply))

                elif message in ['/qiwi','/киви','/баланс']:
                    qiwi = QApi(token=qiwitoken,phone=qiwinum)
                    send('Баланс на QIWI: ' + str(qiwi.balance[0]))

                elif message in ['/b+','/+чс','/ban']:ban(reply)

                elif message in ['/b-','/-чс','/unban']:unban(reply)

                elif message in ['/f+','/+друг','/addfriend']: addfriend(reply)

                elif message in ['/f-','/-друг','/delfriend']: delfriend(reply)

                elif cmd[0] in ['/call','/созвать']:
                    people=vk.messages.getConversationMembers(peer_id=peer_id)['response']['profiles']
                    jn = 0
                    if len(cmd) > 1: jt = '📢 Созыв всех участников беседы\nПричина: '+cmd[1]
                    else: jt = '📢 Созыв всех участников беседы'
                    jt1 = ''
                    jt2 = ''
                    while jn != len(people):
                        if jn > 249: jt2 = jt2 + '[id' + str(people[jn]['id'])+ '|\u200b]'
                        else: jt1 = jt1 + '[id' + str(people[jn]['id'])+ '|\u200b]'
                        jn = jn + 1
                    send(jt + jt1)
                    if jt2 != '': send(jt+jt2)
                else: log_flug = False

                #Автоперевод
            elif autotr and len(message)>1 and log_flug: edit(tr(message))

            if admin and log_flug:
                Log(str(counter), ")\nCMD: " + str(message))
                counter += 1

    # Если что-то сломалось или введела кривая команда            
    except Exception as error:
        time.sleep(1)
        if 'Captcha needed' in str(error):
            print('Капча, ждём 10 сек')
            time.sleep(10)
        elif "FileNotFoundError" in str(error): print("Файл отсутствует ")
        else: print(error)
        msend(error)
        Log(str(counter),  ")\nCMD:\n" + str(message) + "\n\nERR:\n" +  str(error))
        counter += 1