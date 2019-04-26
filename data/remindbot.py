import discord, asyncio, random, datetime
import urllib.request

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
            await message.channel.send('public ip: ' + external_ip)

        if message.content.startswith('..spam'):
            if message.author.id == 493938037189902358:
                return
            msg = message.content.split()
            if len(msg) < 2:
                await message.channel.send('you need to put a message to spam')
            if len(msg) == 2:
                if msg[i] == '@everyone':
                    await message.channel.send('no i\'m not pinging everyone')
                    return
                for i in range(0,5):
                    await message.channel.send(msg[1])
            if len(msg) > 2:
                try:
                    number = int(msg[len(msg)-1])
                except:
                    for i in range(0,5):
                        await message.channel.send(makeStr(msg[1:]))
                    return
                msg.pop(len(msg)-1)
                msg.pop(0)
                pstr = ''
                for item in msg:
                    pstr += item + ' '
                for i in range(0, number):
                    await message.channel.send(pstr)

client = MyClient()
