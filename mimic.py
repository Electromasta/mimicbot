import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import re

from box.table import *
from box.reader import *

client = Bot(description="Test Bot", command_prefix="PPREFIX", pm_help = True)

debug = True
pattern = ("([0-9]\\d*)*[d]([0-9]\\d*)([+-]\\d+)?")
suits = ['Heart', 'Club', 'Spade', 'Diamond']
tables = createTables()

if (debug):
        for table in tables:
               for row in table.rows:
                        print(row.name + "\n" + row.desc)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

@client.command()
async def ping(*args):
	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	await client.say(":warning: Test")

@client.event
async def on_message(message):
    if message.content.startswith('!roll'):
        await client.send_message(message.channel, parseDice(message.content[6:]))
    #elif message.content.startswith('!r'):
    #    await client.send_message(message.channel, parseDice(message.content[3:]))
    if message.content.startswith('!draw'):
        await client.send_message(message.channel, drawCard())
    #elif message.content.startswith('!d'):
    #    await client.send_message(message.channel, drawCard())
    if message.content.startswith('!explore'):
        await client.send_message(message.channel, getEncounter(message.content[9:], True))

def getEncounter(x, isRoot):
   for table in tables:
      if x.lower() in table.name.lower():
         diceroll = random.randrange(1, 100)
         result = ""
         if (isRoot):
            result += table.name + " (" + str(diceroll) + "): "
         name = table.get(diceroll).name
         while (len(name)>0):
            if (name.find("<") != -1):
               result += name[:name.find("<")]
               result += getEncounter(name[name.find("<")+1:name.find(">")], False)
               name = name[name.find(">")+1:]
            else:
               result += name + table.get(diceroll).desc
               name = ""
         return result

   return "Not Found"

def parseDice(x):
    p = re.compile(pattern)

    if p.match(x) is None or p.match(x).group(0) is None:
        return roll(1, 6, 0)

    rolls =  p.match(x).group(1)
    if rolls is None:
        rolls=1
    else:
        rolls = int(rolls)
    sides = int(p.match(x).group(2))
    addition = p.match(x).group(3)
    if addition is None:
        addition=0
    else:
        if addition[:1] == '+':
            addition = int(addition[1:])
        else:
            addition = -int(addition[1:])
    return roll(rolls, sides, addition)

def roll(x, y, z):
    if y>100 or x*y > 241 or x*y < 2:
        return 'No Thanks'
    
    result = "Rolling: ["
    total = 0;
    
    for x in range(0, x):
        r = random.randrange(1, y)
        total += r
        result += str(r) + ', '
    
    tail = ''
    if z < 0:
        tail += str(z)
        total += z
    elif z > 0:
        tail += '+' + str(z)
        total += z

    result = result[:-2] + "]" + tail + " = " + str(total)
    return result

def drawCard():
    suit = random.randrange(0, 3)
    value = random.randrange(1, 13)

    if value==1:
        value = 'Ace'
    elif value == 11:
        value = 'Jack'
    elif value == 12:
        value = 'Queen'
    elif value == 13:
        value = 'King'
    else:
        value = str(value)

    return "Drawing: [The " + value + ' of ' + suits[suit] + 's]'

client.run('NDAzNjYyNjgxNjgyMzQ1OTg1.DUKmOQ.95eg0sAXaHSf_EcQTNIuMwwvtEY')
