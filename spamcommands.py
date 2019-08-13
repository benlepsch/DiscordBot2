import discord, asyncio, re

from token_folder import token
from global_functions import makeStr, minh_id

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
            if message.author.id == minh_id:
                await message.channel.send('no minh you dont get to spam')
                return
            if message.channel.name == 'general' or message.channel.name == 'building-projects':
                await message.channel.send('can\'t spam in ' + message.channel.name)
                return
            if re.search('@everyone', message.content):
                await message.channel.send('no pinging everyone')
                return
            
            msg = message.content.split()
            if len(msg) < 2:
                await message.channel.send('you need to put a message to spam')
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
        
        if message.content.startswith('..dmspam'):
            if message.author.id != 262637906865291264 or message.author.id != 178876334095859712:
                await message.channel.send('you don\'t have permission to do that!')
                return

            msg = message.content.split()
            msg.pop(0)
            
            # ..dmspam -u @user -m <message>

            if len(msg) < 2:
                await message.channel.send('proper message formatting: `..dmspam @user <message>`')
                return
            
            if len(msg) == 2:
                amount = 5
            else:
                amount = int(msg[(len(msg) - 1)])
            msg.pop(len(msg) - 1) 
            pguild = message.author.guild
            
            player_tag = list(msg[0])
            fpt = ''
            #print(player_tag)
            for item in player_tag:
                #print('inting ' + item)
                try:
                    #print(int(item))
                    fpt += str(int(item))
                except:
                    fpt += ''
            #print(fpt)
            fpt = int(fpt)

            to_ping = pguild.get_member(fpt)
            to_send = makeStr(msg[1:])

            for i in range(amount):
                await to_ping.send(to_send)



SpamClient = MyClient()
SpamClient.run(token)
