
# bot.py
import os
import random
from dotenv import load_dotenv

# 1
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True # see members of the server

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# 2
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(f'{bot.user.name} has connected to Discord to {guild}')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name='quack', help='Responds with QUACK')
async def quack(ctx):
    response = 'QUACK'
    await ctx.send(response)

@bot.command(name='quack_rep', help='QUACK with repetitions')
async def quack(ctx, reps: int):
    response = 'QUACK'
    await ctx.send(' '.join([response for _ in range(reps)])) 

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {member.guild.name}! Say "!quack" in Recruit\'s Pond to get some Quacks!'
    )

bot.run(TOKEN)


# bot.py
# import os

# import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

# intents = discord.Intents.default()
# intents.members = True
# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
#     print(f'{client.user.name} has connected to Discord to {guild}')
#     members = '\n - '.join([member.name for member in guild.members])
#     # print(f'Guild Members:\n - {members}')
    


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to {member.guild.name}! Say "hi" in Recruit\'s Pond to get some Quacks!'
#     )

# @client.event
# async def on_message(message):
#     # ignore messages sent by this bot 
#     if message.author == client.user:
#         return 
#     if 'hi' in message.content.lower():
#         await message.channel.send("Quack")
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException

# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Exception message: {args[0]}\n')
#         else:
#             raise



# client.run(TOKEN)

