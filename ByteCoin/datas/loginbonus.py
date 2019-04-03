"""
import datetime
from datas import playerdata
playerdata_class = playerdata.data


class loginbonus:
    def __init__(self, bot):
        self.bot = bot
    async def on_message(self,message):
        mention = '<@!'+message.author.id+'>'
        args = []
        args = message.content.split(' ')
        loginmessage= "logined"

        loginmessage = loginbonus.login(message.author.id)
        if not loginmessage == "logined":
            await self.bot.send_message(message.channel,mention + loginmessage)

################################################################
#  指定したプレイヤーのすべての値を保存
################################################################
    def login(id):
        path = 'datas/loginbonus.txt'
        list = []

        if loginbonus.getdata(id,'last') == -1 and playerdata_class.getdata(id,'coin') != -1:
            addline = id+':'+str(datetime.date.today())+':1\n'
            file = open(path,'r',encoding="utf-8_sig")
            list = file.readlines()
            file.close()

            file = open(path,'w',encoding="utf-8_sig")
            list.append(addline)
            file.writelines(list)
            file.close()

            playerdata_class.addcoin(id,50)
            return("|:clock9:**初ログインありがとう！** `合計:1日目 50枚入手しました`")
        else:
            lastday = str(loginbonus.getdata(id,'last')).split('-')
            now = str(datetime.date.today()).split('-')
            if lastday[0] != now[0] or lastday[1] != now[1] or lastday[2] != now[2]:
                loginbonus.savedata(id)
                coin_amount = 10
                total = loginbonus.getdata(id,'total')
                # 合計ログイン日数bonus
                # Switch文だったらきれいに書けるけどPythonには無いから仕方なくifを連ねる
                if total == 2:
                    coin_amount = coin_amount + 20
                elif total == 3:
                    coin_amount = coin_amount + 30
                elif total == 4:
                    coin_amount = coin_amount + 40
                elif total == 5:
                    coin_amount = coin_amount + 50
                elif total == 7:
                    coin_amount = coin_amount + 90
                elif total == 10:
                    coin_amount = coin_amount + 10
                elif total == 14:
                    coin_amount = coin_amount + 90

                playerdata_class.addcoin(id,coin_amount)
                return("|:clock9:**ログインありがとう！** `合計:"+str(total)+"日目 "+str(coin_amount)+"枚入手しました`")
            return("logined")

################################################################
#  指定したidのデータを読み込む
################################################################
    def getdata(id,mode):
        if mode == 'id':
            list_amount = 0
        if mode == 'last':
            list_amount = 1
        if mode == 'total':
            list_amount = 2

        data = []
        #ファイル内の文字を取得する処理
        path = 'datas/loginbonus.txt'
        file = open(path,'r',encoding="utf-8_sig")

        #　全プレイヤーのデータを取得
        if str(id) == 'all':
            list = file.readlines()
            i=0
            amount = []

            #　データを取得
            for text in list:
                data = text.split(':')
                amount.append(player_data[list_amount].replace('\n', ''))
                i = i + 1
        #　指定したidのデータを取得
        else:
            amount = -1
            list = file.readlines()
            i=0
            #　データを取得
            for text in list:
                list[i] = text.replace('\n', '')

                if id in text:
                    data = text.split(':')
                    if list_amount == 2:
                        amount = int(data[list_amount])
                    else:
                        amount = str(data[list_amount])
                    break
                    i = i + 1
        file.close()
        return(amount)
################################################################
#  指定したidのデータを保存
################################################################
    def savedata(id):
        addline = id+':'+str(datetime.date.today())+':'+str(int(loginbonus.getdata(id,'total'))+1)+'\n'
        # 保存処理
        path = 'datas/loginbonus.txt'
        list = []

        file = open(path,'r',encoding="utf-8_sig")
        list = file.readlines()
        file.close()

        i = 0
        for  text in list:
            if id in text:
                list[i] = addline
                file = open(path,'w',encoding="utf-8_sig")
                file.writelines(list)
                file.close()
            i = i + 1

def setup(bot):
    bot.add_cog(loginbonus(bot))

"""
