# Code Tracker TelegramBot

A magic telegram bot to send you updates from your running code. These updates can includes only a few characteres to a cool image.

# Basic Features!

  - Send messages containg updates from your codes
    - NO REPEATED MESSAGES! If you try to send the same message repeatedly the _sender_ will only send the first one! 
  - Send your images and charts using this bot
  - Cool thread system to not lock and speed down your codes


# Installation

  - Clone this repository and install dependencys
  - If you haven't already, install telegram library
  - This is it


# Configuration

 You'll need to create a bot with https://telegram.me/botfather, this will generate the code to configure the bot. Save it to a fila and remember it's location
 open the files "botter.py" and "send_update.py" to configure the variable "base_path", which is the location the file is stored.
 You also need to configure the location of the key you generated with @botfather on these files

# Utilization

- Run botter.py
- Start a conversation with your bot
- Send the commands to the bot




| Comando       | Descrição    | Parameters |
| ------------- |:-------------:|:-------------:|
| sub           | Subscribe to a list | Name of the subscription |
| subscribe     | Subscribe to a list | Name of the subscription |
| getsubs       | Get a list of your subscription | None |
| get           | Get a list of your subscription | None |
| del           | Remove a subscription from your list | Name of the subscription |
| delSubs       | Remove a subscription from your list | Name of the subscription |


- Update your code to send the notifications

```python
import send_update
bot_telegram = send_update.Enviador()

for i in range(10):
    bot_telegram.envia_notificacao("sub_name", str(i)+"%")

bot_telegram.envia_img("sub_name","./image.png","A cool image")
```

# Todos

All done for now

License
----

GLWT
