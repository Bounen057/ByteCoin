# coding: UTF-8
import random
import time
from datas import playerdata
import defs
defs_class = defs.defs
playerdata_class = playerdata.data

game_name = '【Hundred】'

class Hundred:
    def __init__(self, bot):
        self.bot = bot



    async def on_message(self,message):
        mention = '<@!'+message.author.id+'>'
        args = []
        args = message.content.split(' ')

        if args[0] == '/coingame' or args[0]== '/cg':
            if args[1] == 'hundred' or args[1] == 'h':
                if len(args) == 1:
                    await self.bot.send_message(message.channel, mention+":warning:**/cg s <賭けコイン>**:warning:")
                elif defs_class.is_int(args[2]) == False:
                    await self.bot.send_message(message.channel, mention+":warning:**数値を入力してください**:warning:")
                elif int(args[2]) > playerdata_class.getdata(message.author.id,'coin'):
                    await self.bot.send_message(message.channel, mention+":warning:**所持コインが足りません!**:warning:")
                elif int(args[2]) < 2:
                    await self.bot.send_message(message.channel, mention+":warning:**1以下の値は選択できません**:warning:")
                else:
                    reply = "**:game_die:"+game_name+"　募集:game_die:**" + "```\n" + "募集者:"+message.author.name+"\n" + "賭けコイン:"+str(args[2])+"\n" + "挑戦者:受付中\n"
                    msg = await self.bot.send_message(message.channel,reply + '```')
                    await self.bot.add_reaction(msg, '☑')
                    self.bot.loop.create_task(self.reaction(msg))
                    playerdata_class.addcoin(message.author.id,-1 * int(args[2]))
    #////////////////////////////////////////////////////////////////////////
    # ゲーム -式-
    #////////////////////////////////////////////////////////////////////////
    async def reaction(self,target_msg):
        while True:
            target_reaction = await self.bot.wait_for_reaction(message=target_msg)
            mention = '<@!'+target_reaction.user.id+'>'

            if target_reaction.reaction.emoji == '☑':
                text = []
                text = target_msg.content.split("\n")

                # self.bot自身の処理ではないかチェック
                if target_reaction.user == target_msg.author:
                    pass
                # コインを持っているか判定
                elif int(text[2].replace('賭けコイン:','')) > playerdata_class.getdata(target_reaction.user.id,'coin'):
                    await self.bot.send_message(target_msg.channel, mention+":warning:**所持コインが足りません!**:warning:")
                # 募集者でないかチェック
                elif text[1] == '募集者:'+target_reaction.user.name:
                    await self.bot.send_message(target_msg.channel, mention+":warning:**自分の募集しているゲームに参加できません！**:warning:")
                else:
                    reply = '\n'.join(text)
                    await self.bot.delete_message(target_msg)
                    ##############################################
                    # 本ゲーム処理
                    ##############################################
                    # 変数の用意
                    make_player = text[1].replace('募集者:','')
                    join_player = target_reaction.user.name
                    make_player_mention = '<@!'+playerdata_class.getdata(make_player,'id')+'>'
                    join_player_mention = '<@!'+playerdata_class.getdata(join_player,'id')+'>'
                    sendchannel = target_msg.channel

                    coin = text[2].replace('賭けコイン:','')
                    random_amount = 100
                    playerdata_class.addcoin(playerdata_class.getdata(join_player,'id'),-1 * int(coin))

                    await self.bot.send_message(sendchannel,'**'+game_name+'**'+make_player_mention+':crossed_swords:'+join_player_mention+' :moneybag:賭けコイン:'+coin)
                    await self.bot.send_message(sendchannel, '**'+game_name+'**:game_die:**サイコロ(1~'+str(random_amount)+')を振っています**:game_die:')
                    time.sleep(3)

                    maker_amount = random.randint(1,int(random_amount))
                    await self.bot.send_message(sendchannel, '**'+game_name+'**:game_die:**'+make_player+'>> '+str(maker_amount)+'**:game_die:')
                    joiner_amount = random.randint(1,int(random_amount))
                    await self.bot.send_message(sendchannel, '**'+game_name+'**:game_die:**'+join_player+'>> '+str(joiner_amount)+'**:game_die:')

                    ###########################################
                    #  勝敗判定とその処理
                    ############################################
                    if maker_amount > joiner_amount:
                        await self.bot.send_message(sendchannel, '**'+game_name+'**:tada:**'+make_player_mention+'の勝利! :moneybag:'+str(coin)+'コインGET!**')
                        playerdata_class.addcoin(playerdata_class.getdata(make_player,'id'),int(coin)*2)



                    if maker_amount < joiner_amount:
                        await self.bot.send_message(sendchannel, '**'+game_name+'**:tada:**'+join_player_mention+'の勝利! :moneybag:'+str(coin)+'コインGET!**')
                        playerdata_class.addcoin(playerdata_class.getdata(join_player,'id'),int(coin)*2)


                    if maker_amount == joiner_amount:
                        await self.bot.send_message(sendchannel, '**'+game_name+'**両者引き分け**')
                        playerdata_class.addcoin(playerdata_class.getdata(make_player,'id'),int(coin))
                        playerdata_class.addcoin(playerdata_class.getdata(join_player,'id'),int(coin))

def setup(bot):
    bot.add_cog(Hundred(bot))
