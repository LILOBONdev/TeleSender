# TeleSender 📤

ИСХОДНЫЙ КОД:
```
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
```
> [!NOTE]
> Для запуска программы рассльника не требуется Python. Если отсутствует пакет api-ms-win-core-com-l1-1-0.dll - Попробуйте установить данный пакет. <br> <br>
> Чтобы указать `API-ID`.`API-HASH` - нужно их получить [здесь](https://my.telegram.org/auth?to=apps).

> [!NOTE]
> Программа локальна и никак не застилит ваши данные Telegram аккаунта. Но есть примичание: если вы выйдите со всех устройств, то вам заново приедтся вводить код подтверждения входа в аккаунт со стороны программы

> [!WARNING]
> В случае ошибок программа свернется автоматически. Это может быть вызвано иза: кулдауна в каналае или неккоректных данных указанными вами

> [!TIP]
> Поддержка новых версий программы имеется.
