import discord, asyncio

from token_folder import token, makeStr

class MyClient(discord.Client):

    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

    async def on_message(self, message):
        if message.content.startswith('..spam'):
            if message.author.id == 493938037189902358:
                return
            msg = message.content.split()
            if len(msg) < 2:
                await message.channel.send('you need to put a message to spam')
            if len(msg) == 2:
                if msg[1] == '@everyone':
                    await message.channel.send('no i\'m not pinging everyone')
                    return
                for i in range(0,5):
                    await message.channel.send(msg[1])
            if len(msg) > 2:
                try:
                    number = int(msg[len(msg)-1])
                except:
                    for i in range(0,5):
                        await message.channel.send(makeStr(msg[1:]))
                    return
                msg.pop(len(msg)-1)
                msg.pop(0)
                pstr = ''
                for item in msg:
                    pstr += item + ' '
                for i in range(0, number):
                    await message.channel.send(pstr)
        
        if message.content.startswith('..adminspam'):
            print('called')



SpamClient = MyClient()
SpamClient.run(token)
