# coding: UTF-8
# 現在は利用できない
import random
import time
from datas import playerdata
import defs
defs_class = defs.defs
playerdata_class = playerdata.data
game_name = '[Lottery]'
class lottery:
    def __init__(self, bot):
        self.bot = bot


    async def on_message(self,message):
        mention = '<@!'+message.author.id+'>'
        args = []
        args = message.content.split(' ')

        if args[0] == '/coingame' or args[0]== '/cg':
            if args[1] == 'lottery' or args[1] == 'l':
                if len(args) == -1:
                    await self.bot.send_message(message.channel,'**──Lottery　Help─────────**\n' +
                    '**/cg l <購入枚数> ...**\n' +
                    '`Al`** 1枚10コイン 当たり/170コイン**\n' +
                    '`例`:/cg l 10 Al\n' +
                    '**──────────────────**')
                elif len(args) != 2 and len(args) !=4:
                    await self.bot.send_message(message.channel, mention+":warning:**/cg l <購入枚数> <くじの種類>**:warning:")
                elif len(args) == 4:
                    #エラーチェック
                    if not defs_class.is_int(args[2]):
                        await self.bot.send_message(message.channel, mention+":warning:**適切な値を入力してください /c l**:warning:")
                    amount = int(args[2])
                    if amount < 1:
                        await self.bot.send_message(message.channel, mention+":warning:**適切な値を入力してください /c l**:warning:")
                    elif amount > 50:
                        await self.bot.send_message(message.channel, mention+":warning:**一度でできるのは50回までです**:warning:")
                    #/////////////////////////////////////////////////////
                    #　Al アルタイル - lottery
                    #/////////////////////////////////////////////////////
                    elif args[3] == 'Al':
                        if amount * 10 > playerdata_class.getdata(message.author.id,'coin'):
                            await self.bot.send_message(message.channel, mention+":warning:**所持金が足りません!**:warning:")
                        else:
                            hit = 0
                            for i in range(amount):
                                playerdata_class.addcoin(message.author.id,-10)
                                if random.randint(0,18) == 0:
                                    hit = hit + 1
                            playerdata_class.addcoin(message.author.id,hit * 170)
                            await self.bot.send_message(message.channel, mention+":large_blue_diamond:**結果**`"+str(amount)+"回中 "+str(hit)+"回当選! "+str(hit * 170)+"コインGET`")




def setup(bot):
    bot.add_cog(lottery(bot))
