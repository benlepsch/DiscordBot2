import discord, asyncio, random, datetime
import urllib.request

from token_folder import token

def makeStr(array):
    strr = ''
    for item in array:
        strr += item + ' '
    return strr

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.remind_allah())

    async def remind_allah(self):
        await self.wait_until_ready()
        channel = self.get_channel(541442009957793814)
        while not self.is_closed():
            await channel.send('praise allah :hugging: :hugging:')
            await asyncio.sleep(43200)

    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

        game = discord.Game('obliterating minorities')
        await client.change_presence(status=discord.Status.idle, activity=game)


    async def on_message(self, message):
        if message.content.startswith('am i a coding god'):
            if message.author.id == 262637906865291264:
                print(message)
                print(message.channel)
                await message.channel.send('yes')
            else:
                await message.channel.send('no u suck')

        if message.content.startswith('bot do u work'):
            await message.channel.send('yes PogU')

        if message.content.startswith('..getip') and message.author.id == 262637906865291264:
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            await message.author.send('public ip: ' + external_ip)

client = MyClient()
client.run(token)
