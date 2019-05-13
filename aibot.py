import discord, asyncio, random, re

from token_folder import token
from global_functions import makeStr

def do_i_get_word():
    if random.randint(0,5000) > 4500:
        return True
    return False

def import_words(file='words.txt'):
    words = []
    with open(file, 'r') as word_file:
        words = word_file.read().split()
    return words

def add_word(word, file='words.txt'):
    with open(file, 'a') as word_file:
        word_file.write(' ' + word)

def clear_file(file='words.txt'):
    with open(file, 'w') as word_file:
        word_file.write('bruh')

def say_something():
    words = import_words()
    msg = ''
    for i in range(random.randint(1, 40)):
        msg += words[random.randint(0, len(words)-1)] + ' '
    return msg

def is_it_a_word(word):
    # this is supposed to filter out words that are @ing people or something
    # so structured like <@43985623487> or something

    word = list(word)

    if word[0] == '<' and word[len(word) - 1] == '>': # if it's tagging someone
        return False

    if makeStr(word[0:7]) == 'https://' or makeStr(word[0:6]) == 'http://': # if it's a link like https://youtu.be.something
        return False

    if len(word) > 199: # 199 characters is too long already but this ensures it'll never send something over the message limit
        return False

    return True

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.talk())
    
    async def talk(self):
        global words
        await self.wait_until_ready()
        channel = self.get_channel(541442009957793814)
        while not self.is_closed():
            sleep_time = random.randint(1,600)
            print('talked, sleeping for ' + sleep_time)
            await channel.send(say_something())
            await asyncio.sleep(sleep_time)

    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('..clearfile'):
            clear_file()
            print('cleared word file')
            await message.channel.send('cleared word file')

        if message.content.startswith('..words'):
            with open('words.txt','r') as word_file:
                words = word_file.read()
                await message.channel.send('words in file: ```' + words + '```')

        if message.content.startswith('..delword'):
            words = []
            with open('words.txt','r') as word_file:
                words = word_file.read().split()
                print('words: ')
                print(words)
            to_delete = message.content.split()[1]
            print('deleting ' + to_delete)
            deleted = False
            while not deleted:
                if to_delete in words:
                    print('in words')
                    words.remove(to_delete)
                else:
                    break

            with open('words.txt','w') as word_file:
                word_file.write(makeStr(words))

            await message.channel.send('deleted word ' + to_delete)

        if do_i_get_word():
            msg = message.content.split()
            if len(msg) > 1:
                word_to_get = msg[random.randint(0, (len(msg) - 1))]
            else:
                return
            if is_it_a_word(word_to_get):
                print('new word: ' + word_to_get)
                add_word(word_to_get)
            else:
                print('it wasnt a word: ' + word_to_get)
        
        if re.search('<@493938037189902358>', message.content):
            await message.channel.send(message.author.mention + ' ' + say_something())

AIClient = MyClient()
AIClient.run(token)
