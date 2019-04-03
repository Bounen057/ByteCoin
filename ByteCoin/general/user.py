#################################################################
# <このクラスの説明>
# 一般人用コマンド。誰でも基本使える
#################################################################
import random
import time
from datas  import playerdata
from datas  import ranking
import defs
import discord
playerdata_class = playerdata.data
defs_class = defs.defs
ranking_class = ranking.ranking

class user:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self,message):
        mention = '<@!'+message.author.id+'>'
        args = []
        args = message.content.split(' ')
#///////////////////////////////////////////////////////////////////////////////
# 一般プレイヤー用コマンド
#///////////////////////////////////////////////////////////////////////////////
        if (args[0] == '/coingame' or args[0]== '/cg') and len(args) == 1:
            await self.bot.send_message(message.channel,mention + '|:warning:**使用方法が間違っています! /c help**:warning:')
        if args[0] == '/coin' or args[0]== '/c':

#/////////////////////////////////////////////////////////////////
#   HELPを表示
#/////////////////////////////////////////////////////////////////
            if args[1]=='help':
                await self.bot.send_message(message.channel,'**──ByteCoin【HELP】───────**\n' +
                '**ver β  2019/4/3**\n' +
                '**制作者Twitter @Bounen057**\n' +
                '**/coin...**\n' +
                '`help`** コマンドのHELPを出します**\n' +
                '`profile`** 自分のプロフィールを表示します**\n' +
                '`pay <メンション> <枚数>`**自分のコインを上げます**\n' +
                '`top` **所持コインランキングを表示します**\n' +
                '**/coingame...**\n' +
                '`hundred <賭けコイン数>`** hundredの参加者(1)を募集します**\n' +
                '**─────────────────**')

#/////////////////////////////////////////////////////////////////
#   payコマンド
#/////////////////////////////////////////////////////////////////
            if args[1]=='pay':
                sender = message.author.id
                target = playerdata_class.getid(args[2])
                #エラーチェック
                if len(args) !=4:
                    await self.bot.send_message(message.channel,mention + '|:warning:**使用方法が間違っています! /c pay <メンション> <値>**:warning:')
                elif not defs_class.is_int(args[3]):
                    await self.bot.send_message(message.channel,mention + '|:warning:**適切な値を選択してください! /c help**:warning:')
                elif int(args[3]) <= 0 or int(args[3]) > playerdata_class.getdata(sender,'coin'):
                    await self.bot.send_message(message.channel,mention + '|:warning:**適切な値を選択してください! /c help**:warning:')
                elif playerdata_class.getdata(target,'coin') == -1 or playerdata_class.getdata(sender,'coin') == -1:
                    await self.bot.send_message(message.channel,mention + '|:warning:**方者のデータが存在しません /c l**:warning:')
                else:
                    amount = int(args[3])
                    playerdata_class.addcoin(sender,-1 * amount)
                    playerdata_class.addcoin(target,amount)
                    await self.bot.send_message(message.channel,mention + '|**コインを'+playerdata_class.getdata(target,'name')+'さんに'+str(amount)+'枚送りました!**')



#/////////////////////////////////////////////////////////////////
#   プロフィールを表示
#/////////////////////////////////////////////////////////////////
            if args[1]=='profile' or args[1]=='p':
                await self.bot.send_message(message.channel, mention)
                embed=discord.Embed(title="< "+str(playerdata_class.getdata(message.author.id,'name'))+"s profile >", description="ここにあなたのプロフィールが表示されます", color=0x00ff00)
                embed.set_author(name=''+message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name="Coin:",value = str(playerdata_class.getdata(message.author.id,'coin')), inline=True)
                embed.add_field(name="所持Coinランキング:",value = str(ranking_class.getnumber(message.author.id)))
                await self.bot.send_message(message.channel, embed=embed)


#/////////////////////////////////////////////////////////////////
#   ランキングを表示
#/////////////////////////////////////////////////////////////////
            if args[1]=='top' or args[1]=='t':
                await self.bot.send_message(message.channel,
                ':ribbon: **所持コインランキング TOP5** :ribbon:\n' +
                ':diamond_shape_with_a_dot_inside:**1位**'+ranking_class.getuser(1)+' '+str(ranking_class.getcoin(1))+'枚\n' +
                ':large_blue_diamond:**2位**'+ranking_class.getuser(2)+' '+str(ranking_class.getcoin(2))+'枚\n' +
                ':large_orange_diamond:**3位**'+ranking_class.getuser(3)+' '+str(ranking_class.getcoin(3))+'枚\n' +
                ':small_blue_diamond:**4位**'+ranking_class.getuser(4)+' '+str(ranking_class.getcoin(4))+'枚\n' +
                ':small_orange_diamond:**5位**'+ranking_class.getuser(5)+' '+str(ranking_class.getcoin(5))+'枚\n'
                )



#/////////////////////////////////////////////////////////////////
#   初ログイン者用
#/////////////////////////////////////////////////////////////////
            if args[1]=='login' or args[1]=='l':
                if playerdata_class.saveall(message.author.id,message.author.name,50):
                    await self.bot.send_message(message.channel,'**'+message.author.name+'さんのデータを作成しました! Please \"/c p\"**')
                else:
                    await self.bot.send_message(message.channel,'**'+message.author.name+'さんのデータは既に存在しています。**')




def setup(bot):
    bot.add_cog(user(bot))
