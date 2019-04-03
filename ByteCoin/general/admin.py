######################################################################
# <このクラスの説明>
# Admin用コマンド。通貨の発行など鯖の管理システムが多い
######################################################################
import random
import time
from datas  import playerdata
import defs
import discord
playerdata_class = playerdata.data
defs_class = defs.defs

class admin:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self,message):
        mention = '<@!'+message.author.id+'>'
        args = []
        args = message.content.split(' ')
#///////////////////////////////////////////////////////////////////////////////
# 管理者(Bounen057)用コマンド 通貨の発行権等
#///////////////////////////////////////////////////////////////////////////////
        if args[0] == '/coin' or args[0]== '/c':
            if args[1] == 'admin':
                if message.author.id == '321266537266806784':

#/////////////////////////////////////////////////////////////////////////////
#  HELPを表示
#//////////////////////////////////////////////////////////////////////////////
                    if args[2]=='help':
                        await self.bot.send_message(message.channel,'**──Coin【管理者用コマンドのHELP】─**\n' +
                        '**/coin admin ...**\n' +
                        '`help`** 管理者用コマンドのHELPを出します**\n' +
                        '`add <mention> <amount>`** 指定枚数分コインを増やします**\n' +
                        '`stats`** 統計を表示します**\n' +
                        '**──────────────────**')



#//////////////////////////////////////////////////////////////////////////////
#  メンションしたプレイヤーのコインを増やす(all = 全員)
#//////////////////////////////////////////////////////////////////////////////
                    if args[2] == 'add':
                        id = playerdata_class.getid(args[3])
                        playerdata_class.addcoin(id,args[4])
                        if id == 'all':
                            reply = ':ballot_box_with_check:**全プレイヤー**の所持枚数を**'+str(args[4])+'枚**増加させました！'
                        else:
                            reply = ':ballot_box_with_check:**'+str(playerdata_class.getdata(id,'name'))+'**の所持枚数を**'+str(args[4])+'枚**増加させました！'
                        await self.bot.send_message(message.channel, reply)



#/////////////////////////////////////////////////////////////////////////////
#  鯖の統計情を表示
#/////////////////////////////////////////////////////////////////////////////
                    if args[2] == 'stats':
                        total_coin = 0
                        for coin_amount in playerdata_class.getdata('all','coin'):
                            total_coin = total_coin + int(coin_amount)

                        total_player = 0
                        for i in playerdata_class.getdata('all','id'):
                            total_player = int(total_player) + 1

                        embed=discord.Embed(title="<< Server stats >>", description="サーバーの統計を表示します", color=0x00ff00)
                        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                        embed.add_field(name="総コイン枚数:",value = ''+str(total_coin), inline=True)
                        embed.add_field(name="総プレイヤー数:",value = ''+str(total_player), inline=True)
                        await self.bot.send_message(message.channel, embed=embed)



                else:
                    await self.bot.send_message(message.channel, mention+'|:warning:あなたはこのコマンドを実行する権限がありません:warning:')
def setup(bot):
    bot.add_cog(admin(bot))
