import discord, asyncio, random
from token_folder import token

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as:')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

        self.emotions = ['happy','sad','angry']

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('how are you feeling benbot?'):
            await message.channel.send(self.emotions[random.randint(0,2)])

client = MyClient()
client.run(token)
