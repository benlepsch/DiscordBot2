import discord, asyncio, random, datetime
import urllib.request

from token_folder import token
from global_functions import makeStr

import datetime

remind_hour = 9
last_day_reminded = 30

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.remind_allah())

    async def remind_allah(self):
        await self.wait_until_ready()
        channel = self.get_channel(541442009957793814)
        while not self.is_closed():
            if datetime.datetime.now().time().hour == remind_hour and datetime.datetime.now().day != last_day_reminded:
                await channel.send('praise allah :hugging: :hugging:')
                last_day_reminded == datetime.datetime.now().day

    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

        game = discord.Game('obliterating minorities')
        await client.change_presence(status=discord.Status.idle, activity=game)


    async def on_message(self, message):
        if message.content.startswith('am i a coding god'):
            if message.author.id == 262637906865291264:
                print(message)
                print(message.channel)
                await message.channel.send('yes')
            else:
                await message.channel.send('no u suck')

        if message.content.startswith('bot do u work'):
            await message.channel.send('yes PogU')

        if message.content.startswith('..getip') and message.author.id == 262637906865291264:
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            await message.author.send('public ip: ' + external_ip)

client = MyClient()
client.run(token)
