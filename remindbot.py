import discord, asyncio, random, datetime

from token_folder import token

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
                last_day_reminded = datetime.datetime.now().day
            else:
                await asyncio.sleep(1)

    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')


client = MyClient()
client.run(token)
