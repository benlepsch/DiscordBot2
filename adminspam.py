import discord, asyncio

from token_folder import token
from global_functions import makeStr

dova_id = 262637906865291264

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

    async def on_message(self, message):
        if message.content.startswith('..adminspam'):
            if message.author.id != 262637906865291264:
                await message.channel.send('you don\'t have permission to do that')
                return
            
            msg = message.content.split()
            msg.pop(0)

            # 40 <message>

            if len(msg) == 1:
                await message.channel.send(msg[0])
                return
            
            if len(msg) > 1:
                try:
                    number = int(msg[0])
                except:
                    await message.channel.send('incorrect syntax: should be `..adminspam <number> <msg>`')
                
                spamstr = makeStr(msg[1:])
                for i in range(number):
                    await message.channel.send(spamstr)

client = MyClient()
client.run(token)
