import subprocess

import discord, asyncio
import urllib.request

from token_folder import token
from global_functions import owner, makeStr, users_who_can_get_ip

spam_bot = subprocess.Popen(['python3','./spamcommands.py'])

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')
        
        game = discord.Game('obliterating minorities')
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('am i a coding god'):
            if message.author.id == owner:
                await message.channel.send('yes')
            else:
                await message.channel.send('no u suck')

        for word in message.content.split():
            if 'bruh' in word.lower():
                await message.channel.send('bruh moment')
                break

        if message.content.startswith('bot do u work'):
            await message.channel.send('yes PogU')
        
        if message.content.startswith('..getip') and message.author.id in users_who_can_get_ip:
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            await message.author.send('public ip: ' + external_ip)

        if message.content.startswith('..stopspam'):
            global spam_bot
            spam_bot.kill()
            await message.channel.send('stopped spam bot, restarting now')
            spam_bot = subprocess.Popen(['python3', './spamcommands.py'])

client = MyClient()
client.run(token)
