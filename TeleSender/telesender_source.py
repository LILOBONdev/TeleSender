from pyrogram import Client, filters,types
from time import sleep

try:
    GetChannels,GetApiId,GetHashId,GetNumber,GetUser,repat,text,interval = str(input('Enter channels: ')),int(input('Enter API-ID: ')),str(input('Enter HASH-ID: ')),str(input('Enter phone number: ')),str(input('Enter user: ')),int(input('Enter the number of repetitions: ')),str(input('Enter text: ')),int(input('Enter interval: '))
    bot = Client(name=GetUser, api_id=GetApiId, api_hash=GetHashId, phone_number=GetNumber)
    bot.start()
    for tick in range(repat):
        sleep(interval)
        for i in GetChannels.split():
            print(f'Отправлено в {i} [{tick}/{str(repat)}]')
            bot.send_message(chat_id=i, text=text)
except Exception as ex:
    print(f"ERROR: {ex}")
