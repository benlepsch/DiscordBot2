import discord, asyncio, random
from token_folder import token
from PyDictionary import PyDictionary

banned_channels = ['general']
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
        
        if message.content.startswith('..ban'):
            if message.content.split()[1] in banned_channels:
                return
            banned_channels.append(message.content.split()[1])

        if message.content.startswith('..unban'):
            if not message.content.split()[1] in banned_channels:
                return
            banned_channels.remove(message.content.split()[1])

        if message.channel.name in banned_channels:
            return

        if (random.randint(0,3) == 2):
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
