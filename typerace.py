import discord, asyncio, time, calendar, random
from token_folder import token

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

        self.racing = False
        self.raceStart = 0
        self.msg = ''

        enc = list('𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫 \'-𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘.,&')
        reg = list('abcdefghijklmnopqrstuvwxyz \'-1234567890.,&')
        self.conv = {}
        for i in range(len(reg)):
            self.conv[reg[i]] = enc[i]
    
    def convert(self, msg):
        msg = list(msg)
        out = ''
        for l in msg:
            out += self.conv[l]
        
        return out
    
    def genMsg(self):
        f = open('words_alpha.txt').read().split('\n')
        out = ''
        for i in range(random.randint(5,20)):
            out += ' ' + random.choice(f)
        self.msg = out[1:]
        return out[1:]
        

    async def on_message(self, message):
        if self.user.id == message.author.id:
            return
        
        if message.content.startswith('..typerace'):
            if self.racing:
                await message.channel.send('theres already a race going on')
                return
            self.racing = True
            s = self.genMsg()
            self.raceStart = calendar.timegm(time.gmtime())
            await message.channel.send(self.convert(s))

        if message.content == self.msg:
            self.racing = False
            self.msg = ''
            t = calendar.timegm(time.gmtime()) - self.raceStart
            await message.channel.send('race over! ' + message.author.mention + ' won in ' + str(t) + ' seconds.')

        if message.content.startswith('..stop'):
            self.racing = False
            self.raceStart = 0
            self.msg = ''

client = MyClient()
client.run(token)
