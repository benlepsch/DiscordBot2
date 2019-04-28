import discord, asyncio, random

def do_i_get_word():
    if random.randint(0,5000) > 2500:
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

    if word[0] == '<' and word[len(word) - 1] == '>':
        # it's tagging someone
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
        
        if do_i_get_word():
            msg = message.content.split()
            word_to_get = msg[random.randint(0, (len(msg) - 1))]
            if is_it_a_word(word_to_get):
                print('new word: ' + word_to_get)
                add_word(word_to_get)
            else:
                print('it wasnt a word: ' + word_to_get)
        
        msg = message.content.split()
        if '<@493938037189902358>' in msg:
            await message.channel.send(message.author.mention + ' ' + say_something())

AIClient = MyClient()
AIClient.run('NDkzOTM4MDM3MTg5OTAyMzU4.DvcWkw.u8_xud6Esb6VQl3GCkkv5___MzM')
