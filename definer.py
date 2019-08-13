import discord, asyncio, random
from token_folder import token
from PyDictionary import PyDictionary

dictionary = PyDictionary()

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if (random.randint(0,5) == 4):
            msg = message.content.split()
            todefine = msg[random.randint(0, len(msg) - 1)]
            try:
                await message.channel.send('**' + todefine + '** means ' + dictionary.meaning(todefine)['Noun'][0])
            except:
                try:
                    await message.channel.send('**' + todefine + '** means ' + dictionary.meaning(todefine)['Verb'][0])
                except:
                    await message.channel.send('Couldn\'t find a definition for ' + todefine)

client = MyClient()
client.run(token)
