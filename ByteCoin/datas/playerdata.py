# coding: UTF-8
#######################################################################
# [playerdata.py]
#主にdata.txtの操作に関する関数です
#関数の使い方はそれぞれ関数が定義されている１つ上の行をみてください
#######################################################################
from datetime import datetime

class data:
################################################################
#  指定したプレイヤーのすべての値を保存
################################################################
    def saveall(id,name,coin_amount):
        coin_amount = int(coin_amount)
        path = 'datas/playerdata.txt'
        list = []
        addline = id+':'+name+':'+str(0)+'\n'

        if data.getdata(id,'coin') == -1:
            file = open(path,'r',encoding="utf-8_sig")
            list = file.readlines()
            file.close()

            file = open(path,'w',encoding="utf-8_sig")
            list.append(addline)
            file.writelines(list)
            file.close()
            return(True)
        else:
            return(False)


################################################################
#  指定したidのデータを読み込む
################################################################
    def getdata(id,mode):
        if mode == 'id':
            list_amount = 0
        if mode == 'name':
            list_amount = 1
        if mode == 'coin':
            list_amount = 2

        player_data = []
        #ファイル内の文字を取得する処理
        path = 'datas/playerdata.txt'
        file = open(path,'r',encoding="utf-8_sig")


        #　全プレイヤーのデータを取得
        if str(id) == 'all':
            list = file.readlines()
            i=0
            amount = []

            #　データを取得
            for text in list:
                player_data = text.split(':')
                if mode=='coin':
                    amount.append(int(player_data[list_amount].replace('\n', '')))
                else:
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
                    player_data = text.split(':')
                    if list_amount == 2:
                        amount = int(player_data[list_amount])
                    else:
                        amount = str(player_data[list_amount])
                    break
                    i = i + 1
        file.close()
        return(amount)


################################################################
#  指定したidのデータを保存
################################################################
    def savedata(id,mode,data_amount):
        if mode == 'name':
            addline = id+':'+data_amount+':'+data.getdata(id,'coin')+'\n'
        if mode == 'coin':
            addline = id+':'+str(data.getdata(id,'name'))+':'+str(data_amount)+'\n'
        # 保存処理
        path = 'datas/playerdata.txt'
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


###################################################
#  メンションからidを取得
###################################################
    def getid(mention):
        mention = mention.replace('<','')
        mention = mention.replace('>','')
        mention = mention.replace('!','')
        mention = mention.replace('@','')
        return(mention)


###################################################
# 他人のプレイヤーのコインを指定枚数分増やす
###################################################
    def addcoin(id,amount):
        if id == 'all':
            for player in data.getdata('all','id'):
                data.savedata(player,'coin',data.getdata(player,'coin') + int(amount))

        else:
            print('['+str(datetime.now().strftime("%Y/%m/%d %H:%M"))+']'+str(data.getdata(id,'name'))+'の所持コインを'+str(amount)+'枚増加')
            coin_amount = data.getdata(id,'coin')
            coin = coin_amount + int(amount)
            data.savedata(id,'coin',coin)
