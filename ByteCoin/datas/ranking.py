from datas  import playerdata
import numpy as np
playerdata_class = playerdata.data

class ranking:
    def getuser(amount):
        users = playerdata_class.getdata('all','name')
        coin = playerdata_class.getdata('all','coin')

        total = list(zip(coin,users))
        total.sort()
        total.reverse()

        return(total[int(amount)-1][1])

    def getcoin(amount):
        users = playerdata_class.getdata('all','name')
        coin = playerdata_class.getdata('all','coin')

        total = list(zip(coin,users))
        total.sort()
        total.reverse()

        return(total[int(amount)-1][0])

    def getnumber(id):
        ids = playerdata_class.getdata('all','id')
        coin = playerdata_class.getdata('all','coin')

        total = list(zip(coin,ids))
        total.sort()
        total.reverse()
        for i in range(len(coin)):
            if id in total[i][1]:
                break
        return(i+1)

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(ranking(bot))
