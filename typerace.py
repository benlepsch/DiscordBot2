import discord, asyncio, datetime
from token_folder import token

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

        self.type_racing = False
        self.type_racing_start = 0

    async def on_message(self, message):
        if self.user.id == message.author.id:
            return


