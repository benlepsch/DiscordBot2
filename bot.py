import subprocess, re

import discord, asyncio
import urllib.request

from token_folder import token
from global_functions import owner, makeStr, users_who_can_get_ip, get_sohn_config, is_sohn_in_word, sohn_top

spam_bot = subprocess.Popen(['python3','./spamcommands.py'])

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')
        
        game = discord.Game('obliterating minorities')
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('am i a coding god'):
            if message.author.id == owner:
                await message.channel.send('yes')
            else:
                await message.channel.send('no u suck')
        
        sohning = False
        sending = ''
        for word in message.content.split():
            if is_sohn_in_word(word.lower()) != 'not sohn':
                sending += is_sohn_in_word(word.lower())
                sending += '\n'
                sohning = True
        
        if sohning:
            await message.channel.send(sending)

        for word in message.content.split():
            if re.search('so', word.lower()) and is_sohn_in_word(word.lower()) == False:
                await message.channel.send(sohn_top())
                return
            if '~bruh' in word.lower():
                await message.channel.send('b̶̧̙͔̪̩͙̖̩̺͔̣̭̈́̈́̌̅̀̉̑̾͑͆̕͠r̷̠̓ù̸̜̼̤̼͕̣̱̣̣̜̱͓̹̳̃̀̀̀̀͐̊̿̉̐̌͊͑͘ḣ̴̨̢͎̯̞̤̫͉͔̥͎̋͌͆͆̉̍̾͑̑͠͝ ̸̬̘͈̲͖̅̐̋̐̔̄͂̒̿͂͗͋̈́̿̕͜m̵̛̛̛̪̗͔̘̓͆̈̕o̷̢̖̝̬͉͌̋̊̋͐̄̍͘ͅm̸̨̩͍͇̮͇͙͙̥̥̈́͑̂̀͛͌̽̈̈́̎̏͠e̴͚̮̤̎̏̅̓͆̅̕n̴̛͇̟̦̳̤̥̜̮̮͆̒̀̎̀̈́̋̈́̃̿͋̚ͅt̷̛͍̲̼͆̅̃̏̍̑̀')
                return
            if 'bruh' in word.lower():
                await message.channel.send('bruh moment')
                return
            
        if message.content.startswith('bot do u work'):
            await message.channel.send('yes PogU')
        
        if message.content.startswith('..getip') and message.author.id in users_who_can_get_ip:
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            await message.author.send('public ip: ' + external_ip)

        if message.content.startswith('..stopspam'):
            global spam_bot
            spam_bot.kill()
            await message.channel.send('stopped spam bot, restarting now')
            spam_bot = subprocess.Popen(['python3', './spamcommands.py'])

client = MyClient()
client.run(token)
