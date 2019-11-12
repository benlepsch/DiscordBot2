import discord, asyncio, subprocess, re
from token_folder import token

def stringOutputHandler(input):
    return ('' if input == None else '\n'.join(str(input)[2:-1].split('\\n')))

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('$c'):
            msg = message.content.split()
            msg.pop(0)
            print(' '.join(msg))

            cmd = subprocess.Popen(msg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, stderr = cmd.communicate()
            await message.channel.send('```\n' + stringOutputHandler(stdout) + '\n' + stringOutputHandler(stderr) + '\n```')

client = MyClient()
client.run(token)