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

        enc = list('𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫 \'-𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘.,&')
        reg = list('abcdefghijklmnopqrstuvwxyz \'-1234567890.,&')
        self.conv = {}
        for i in range(reg):
            self.conf[reg[i]] = enc[i]
    
    def convert(msg):
        msg = list(msg)
        out = ''
        for l in msg:
            out += conv[l]
        
        return out
    
    def genMsg():
        f = open('words_alpha.txt').read().split('\n')
        out = ''
        for i in range(random.randint(5,20)):
            out += ' ' + random.choice(f)
        return out[1:]
        

    async def on_message(self, message):
        if self.user.id == message.author.id:
            return
        
        if message.content.startswith('..typerace'):
            self.racing = True
            self.raceStart = calendar.timegm(time.gmtime())
            await message.channel.send(self.convert(self.genMsg()))

        if message.content.startswith('..typerace'):
            self.racing = False
            self.raceStart = 0