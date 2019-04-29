import discord, asyncio

from token_folder import token, makeStr

def get_todos(file='todos.txt'):
    todofile = open(file, 'r')
    contents = todofile.read().split('\n')
    todofile.close()
    return contents

def add_todo(todo, file='todos.txt'):
    todofile = open(file, 'r')
    contents = todofile.read().split()
    
    if todo in contents:
        return('that todo already exists')
    
    todofile.close()

    todofile = open(file, 'a')
    todofile.write('\n' + todo)
    todofile.close()
    return('successfully added todo `{}`'.format(todo))

def del_todo(todo, file='todos.txt'):
    todofile = open(file, 'r')
    todo = todo.split()[0]

    current_todos = todofile.read().split()
    todofile.close()

    removed = False

    for thing in current_todos:
        print('comparing {} and {}.'.format(thing, todo))
        if str(thing) == str(todo):
            print('they are equal, removing {}'.format(todo))
            current_todos.remove(todo)
            removed = True
    
    if not removed:
        return('`{}` isn\'t in the todos file'.format(todo))
    
    todofile = open(file, 'w')
    todofile.write(makeStr(current_todos, '\n'))
    todofile.close()
    return('successfully delted todo `{}`'.format(todo))

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('..addtodo'):
            await message.channel.send(add_todo(makeStr(message.content.split()[1:])))

        if message.content.startswith('..todos'):
            await message.channel.send('todos: ``` {}```'.format(makeStr(get_todos(), '\n')))
        
        if message.content.startswith('..deltodo'):
            await message.channel.send(del_todo(makeStr(message.content.split()[1:])))
        
        if message.content.startswith('..cleartodos'):
            todofile = open('todos.txt', 'w')
            todofile.write('\n')
            todofile.close()
            await message.channel.send('cleared todos')

client = MyClient()
client.run(token)