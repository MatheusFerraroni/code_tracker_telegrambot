from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import json, os, datetime


base_path = "~/Documents/telegram_bot/"



def doSubscribe(bot,update):
    chat_id = update.message.chat_id
    msg = update["message"]["text"]


    msg = msg.split(" ")
    if len(msg)!=2:
        bot.sendMessage(chat_id=chat_id, text="Parametros invalidos :-(")
        return
    else:
        try:
            chat_id = str(chat_id)
            file_dest = base_path+"subs/"
            if not os.path.isdir(file_dest):
                os.mkdir(file_dest)
            file_dest += chat_id
            sub = os.path.isfile(file_dest)


            if not sub:
                ativodate = datetime.datetime.now()
                ativodate = str(ativodate)
                obj = {"cod":chat_id,"status":"ativo","cadastro":ativodate,"desativo":None,"inscritos":[msg[1]],"mensagens_enviadas":{}}
                aarquivo = open(file_dest,"w")
                aarquivo.write(json.dumps(obj))
                aarquivo.close()
            else:
                aarquivo = open(file_dest,"r")
                infos = json.loads(aarquivo.read())
                aarquivo.close()

                if msg[1] not in infos["inscritos"]:
                    infos["inscritos"].append(msg[1])
                    aarquivo = open(file_dest,"w")
                    aarquivo.write(json.dumps(infos))
                    aarquivo.close()
                else:
                    bot.sendMessage(chat_id=chat_id, text="Ja inscrito!")
                    return

            bot.sendMessage(chat_id=chat_id, text="Inscrissao realizada com sucesso")
        except Exception as e:
            bot.sendMessage(chat_id=chat_id, text=str(e))


        return

def getSubs(bot,update):
    chat_id = update.message.chat_id
    chat_id = str(chat_id)
    try:
        file_dest = base_path+"subs/"
        if not os.path.isdir(file_dest):
            os.mkdir(file_dest)
        file_dest += chat_id
        sub = os.path.isfile(file_dest)
        if not sub:
            bot.sendMessage(chat_id=chat_id, text="Voce ainda nao se inscreveu em nada")
        else:
            aarquivo = open(file_dest,"r")
            infos = json.loads(aarquivo.read())
            aarquivo.close()

            inscricoes = "Suas inscricoes:\n"
            for m in infos["inscritos"]:
                inscricoes += "     @"+m+"\n"

            bot.sendMessage(chat_id=chat_id, text=inscricoes)

        return
    except Exception as e:
        bot.sendMessage(chat_id=chat_id, text=str(e))
        return


def delSubs(bot,update):
    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    msg = update["message"]["text"]
    msg = msg.split(" ")
    if len(msg)!=2:
        bot.sendMessage(chat_id=chat_id, text="Parametros invalidos :-(")
        return
    sair = msg[1]


    try:
        file_dest = base_path+"subs/"
        if not os.path.isdir(file_dest):
            os.mkdir(file_dest)
        file_dest += chat_id
        sub = os.path.isfile(file_dest)
        if not sub:
            bot.sendMessage(chat_id=chat_id, text="Voce ainda nao se inscreveu em nada")
            return
        else:
            aarquivo = open(file_dest,"r")
            infos = json.loads(aarquivo.read())
            aarquivo.close()

            try:
                infos["inscritos"].remove(sair)
            except:
                pass
            aarquivo = open(file_dest,"w")
            aarquivo.write(json.dumps(infos))
            aarquivo.close()

            bot.sendMessage(chat_id=chat_id, text="Inscricao em @"+sair+" cancelada")


        return
    except Exception as e:
        bot.sendMessage(chat_id=chat_id, text=str(e))
        return


def main():
    file = open("~/apis/telegram","r")
    key = file.read()
    file.close()

    updater = Updater(key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('sub',doSubscribe))
    dp.add_handler(CommandHandler('subscribe',doSubscribe))
    dp.add_handler(CommandHandler('getsubs',getSubs))
    dp.add_handler(CommandHandler('get',getSubs))
    dp.add_handler(CommandHandler('del',delSubs))
    dp.add_handler(CommandHandler('delSubs',delSubs))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()