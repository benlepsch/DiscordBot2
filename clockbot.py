import discord, asyncio, random, datetime
import time

from token_folder import token

import datetime


remind_hour = 9
last_day_reminded = 30

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

    async def on_message(self, message):
        if message.content.startswith('clockbot more like cockbot'):
            await message.channel.send('fuck you')
        
        if message.content.startswith('start clock'):
            while True:
                await message.channel.send('it is now ' + str(datetime.datetime.now()))
                time.sleep(1)

client = MyClient()
client.run(token)
