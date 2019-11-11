import discord, asyncio
from minesweeper import Minesweeper

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
        
        if message.content.startswith('..startgame'):
            return(self.ms.startGame(''.join(message.content.split()[1:])))
        
        if message.content.startswith('..break'):
            self.ms.clear(message.content.split()[1])
        
        if message.content.startswith('..flag'):
            self.ms.flag(message.content.split()[1])