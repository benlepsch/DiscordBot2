Sup

this is a git thing for my discord bot so i don't lose all my progress


i use python3 and discord.py rewrite to make my bot

discord.py rewrite api link here:
https://discordpy.readthedocs.io/en/latest/ext/commands/api.html

discord.py rewrite github link here:
https://github.com/Rapptz/discord.py/tree/rewrite/

the bot is structured in different files that all run on the same token so i can edit parts of the bot without taking it down completely
e.g. if i want to change the time the remind bot sends a message at i don't have to take down the part of the bot recording words said

I use tmux to run the different bot sections so i don't have to keep open multiple terminal sessions

my token is a separate package that isn't pushed to github (it's just token\_folder/\_\_init\_\_.py and \_\_init\_\_.py is one line with "token='\<token here\>'"

