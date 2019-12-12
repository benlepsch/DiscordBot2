import discord, asyncio
import urllib.request
from token_folder import token
from global_functions import users_who_can_get_ip

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

    async def on_message(self, message):
        try:
            if message.author.id == self.user.id:
                return

            if message.author.id not in users_who_can_get_ip:
                return

            if message.content.startswith('..getip'):
                external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
                await message.author.send('public ip: ' + external_ip)

            if message.content.startswith('..vaughnserverip'):
                await message.author.send('216.192.76.25')
        except:
            print('oopies we had a fucky wucky')

client = MyClient()
client.run(token)
