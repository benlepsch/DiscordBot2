import discord, asyncio
import urllib.request

from token_folder import token
from global_functions import makeStr, users_who_can_get_ip

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')
        
        game = discord.Game('obliterating minorities')
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        if message.content.startswith('am i a coding god'):
            if message.author.id == 262637906865291264:
                await message.channel.send('yes')
            else:
                await message.channel.send('no u suck')

        if message.content.startswith('bot do u work'):
            await message.channel.send('yes PogU')
        
        if message.content.startswith('..getip') and message.author.id in users_who_can_get_ip:
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            await message.author.send('public ip: ' + external_ip)

client = MyClient()
client.run(token)
