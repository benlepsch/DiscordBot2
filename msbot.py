import discord, asyncio
from minesweeper import Minesweeper
from token_folder import token

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')
        self.ms = Minesweeper()
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        # ..startgame 10 10 15 5d
        if message.content.startswith('..startgame'):
            self.ms.startGame(' '.join(message.content.split()[1:]))
            self.ms.clear(self.ms.firstMove)
            print(self.ms.nicePrint(self.ms.numbersGrid))
            await message.channel.send(self.ms.showGrid())
        if message.content.startswith('..break'):
            await message.channel.send(self.ms.clear(message.content.split()[1]))
        
        if message.content.startswith('..flag'):
            await message.channel.send(self.ms.flag(message.content.split()[1]))
        
        if message.content.startswith('..reset'):
            self.ms.reset()
            await message.channel.send('ok')

client = MyClient()
client.run(token)
