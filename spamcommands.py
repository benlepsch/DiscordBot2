import discord, asyncio, re

from token_folder import token
from global_functions import banned_channels, owner, makeStr, minh_id

class MyClient(discord.Client):

    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('..banned'):
            await message.channel.send('channels banned: ' + ' '.join(banned_channels))
            return

        if message.content.startswith('..ban'):
            if not message.content.split()[1] in banned_channels:
              banned_channels.append(message.content.split()[1])
              await message.channel.send('added channel **{}** to ban list'.format(message.content.split()[1]))
            else:
                await message.channel.send('channel **{}** already banned'.format(message.content.split()[1]))
        
        if message.content.startswith('..unban'):
            if not message.content.split()[1] in banned_channels:
                await message.channel.send('channel **{}** not banned'.format(message.content.split()[1]))
            else:
                banned_channels.remove(message.content.split()[1])
                await message.channel.send('channel **{}** unbanned'.format(message.content.split()[1]))

        if message.channel.name in banned_channels:
            return

        if message.content.startswith('..spamall'):
            channels = message.guild.channels
            print(channels)

            try:
                times = int(message.content.split()[len(message.content.split) - 1])
            except:
                times = 5
            print(times)
            
            for channel in channels:
                print('trying channel ' + str(channel))
                if channel in banned_channels:
                    print('channel is banned, skipping')
                    continue
                try:
                    for i in range(times):
                        await channel.send(' '.join(message.content.split()[1:-1]))
                except:
                    print('failed')
            print('done')
            return

        if message.content.startswith('..spam'):
            if message.author.id == 493938037189902358:
                return
            if message.author.id == minh_id:
                await message.channel.send('no minh you dont get to spam')
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
            if message.author.id != owner:    
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
