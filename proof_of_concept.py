from token_folder import token 
import discord, asyncio

class Test():
    def __init__(self, n):
        self.n = n
    
    def inc(self):
        self.n += 1
    
    def show(self):
        return self.n

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')
        self.t = Test(0)
    
    async def on_message(self, message):
        if message.author.id == self.user.d:
            return
        
        if message.content.startswith('..show'):
            await message.channel.send('n is ' + str(self.t.show()))
        
        if message.content.startswith('..inc'):
            self.t.inc()

client = MyClient()
client.run(token)
        