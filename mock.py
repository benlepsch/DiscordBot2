import discord, asyncio
from token_folder import token
from global_functions import getID

mocking = 1

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

    async def on_message(self, message):
        global mocking
        
        if message.author.id == self.user.id:
            return
        
        if message.author.id == mocking:
            await message.channel.send(message.content)
        
        if message.content.startswith('..mock'):
            try:
                mocking = getID(message.content.split()[1])
                await message.channel.send('now mocking ' + message.content.split()[1])
            except:
                await message.channel.send('oopsie doopsies we errored')

client = MyClient()
client.run(token)
