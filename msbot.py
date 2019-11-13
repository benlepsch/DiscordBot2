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
            return self.ms.showGrid()
        if message.content.startswith('..break'):
            self.ms.clear(message.content.split()[1])
        
        if message.content.startswith('..flag'):
            self.ms.flag(message.content.split()[1])

client = MyClient()
client.run(token)
