import telegram
import os
import json
import threading



_arquivolock = threading.Lock()
base_path = "~/Documents/telegram_bot/subs/"


def envia(bot,processo,mensagem):
    for filename in os.listdir(base_path):
        try:
            file_path =  base_path+filename
            _arquivolock.acquire()
            file = open(file_path,"r")
            infos = json.loads(file.read())
            file.close()
            _arquivolock.release()
            envia = None
            
            if processo in infos["inscritos"]:
                primeira = None
                try:
                    infos["mensagens_enviadas"][processo]
                    primeira = False
                except:
                    primeira = True

                if primeira==True:
                    infos["mensagens_enviadas"][processo] = mensagem
                    envia = True
                elif primeira==False:
                    if infos["mensagens_enviadas"][processo]==mensagem:
                        envia = False
                    else:
                        infos["mensagens_enviadas"][processo] = mensagem
                        envia = True



            _arquivolock.acquire()
            file = open(file_path,"w")
            file.write(json.dumps(infos))
            file.close()
            _arquivolock.release()

            if envia:
                msg = ""
                msg += "`"+processo+":` "+mensagem

                # print mensagem
                bot.sendMessage(
                    chat_id=infos["cod"],
                    text=msg,
                    parse_mode=telegram.ParseMode.MARKDOWN)

        except Exception as e:
            a = open(base_path+"erros","a")
            a.write(mensagem+"\n")
            a.write(str(e)+"\n")
            a.close()
            raise



def enviaImg(bot, processo, img, mensagem):
    for filename in os.listdir(base_path):
        try:
            file_path =  base_path+filename
            _arquivolock.acquire()
            file = open(file_path,"r")
            infos = json.loads(file.read())
            file.close()
            _arquivolock.release()
            envia = None
            
            if processo in infos["inscritos"]:
                msg = ""
                msg += "`"+processo+":` "+mensagem
                bot.sendMessage(
                    chat_id=infos["cod"],
                    text=msg,
                    parse_mode=telegram.ParseMode.MARKDOWN)
                bot.send_photo(chat_id=infos["cod"], photo=open(img, 'rb'))
        except Exception as e:
            a = open(base_path+"erros","a")
            a.write(str(e)+"\n")
            a.close()
            raise


class Enviador():
    def __init__(self):

        file = open("~/apis/telegram","r")
        key = file.read()
        file.close()

        self.bot = telegram.Bot(token=key)



    def envia_notificacao(self, processo, mensagem):
        t = threading.Thread(target=envia,args=[self.bot,processo,mensagem])
        t.start()
        return

    def envia_img(self, processo, img, msg):
        t = threading.Thread(target=enviaImg,args=[self.bot,processo,img,msg])
        t.start()
        return


# if __name__ == '__main__':
#     e = Enviador()


#     for i in range(10):
#         e.envia_notificacao("devteste",str(i)+"%")

#     print "Fim"


