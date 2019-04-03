######################################################################
# <このクラスの説明>
# staff(社員)用コマンド かなり厳重に管理しなければいけない
######################################################################
import random
import time
from datas  import playerdata
import defs
import discord
playerdata_class = playerdata.data
defs_class = defs.defs

class staff:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self,message):
        mention = '<@!'+message.author.id+'>'
        args = []
        args = message.content.split(' ')
        if args[0] == '/coin' or args[0]== '/c':
            if args[1] == 'staff' or args[1] == "s":
                #　役職「STAFF」を所持しているか確認
                role_names = [role.name for role in message.author.roles]
                if not "STAFF" in role_names:
                    await self.bot.send_message(message.channel, mention+'|:warning:あなたはこのコマンドを実行する権限がありません:warning:')
                else:
#
# ぷれいやーにコインを渡す
# /c s  give <mention> <amount>
#
                    if args[2] == "give":
                        id = playerdata_class.getid(args[3])
                        playerdata_class.addcoin(id,args[4])
                        reply = ':ballot_box_with_check:**'+str(playerdata_class.getdata(id,'name'))+'**の所持枚数を**'+str(args[4])+'枚**増加させました！'
                        await self.bot.send_message(message.channel, reply)
#
#  プレイヤーからコインを徴収
#
                    if args[2] == "remove":
                        id = playerdata_class.getid(args[3])
                        playerdata_class.addcoin(id,int(args[4]) * -1)
                        reply = ':ballot_box_with_check:**'+str(playerdata_class.getdata(id,'name'))+'**の所持枚数を**'+str(args[4])+'枚**徴収しました！'
                        await self.bot.send_message(message.channel, reply)
#
#  HELPを表示
#
                    if args[2]=='help':
                        await self.bot.send_message(message.channel,'**──Coin【管理者用コマンドのHELP】─**\n' +
                        '**/coin staff ...**\n' +
                        '`give <mention> <amount>`** コインをユーザーに渡します(換金)**\n' +
                        '`remove <mention> <amount>`** ユーザーからコインを徴収します(換金)**\n' +
                        '**──────────────────**')



def setup(bot):
    bot.add_cog(staff(bot))
