# coding: UTF-8
import random
import time
from datas import playerdata
from datas import ranking
import defs
import discord
from discord.ext import commands
import traceback
defs_class = defs.defs
playerdata_class = playerdata.data
ranking_class = ranking.ranking
bot = commands.Bot(command_prefix='?')
initial_extensions = [
'games.hundred','general.user','general.staff','general.admin','datas.ranking','games.lottery'
]
token = 'NTA5Mzc2NjEyNzk0NjMwMTQ0.Dt2KSw.7SH_2c10BdYJE5kvWbCYvSi9DOU'

# 起動時に通知してくれる処理
@bot.event
async def on_ready():
    print('---------------')
    print('Logined!')
    print('---------------')


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception:
            traceback.print_exec()
    bot.run(token)
