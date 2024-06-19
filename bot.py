
# bot.py
import os
import random
from dotenv import load_dotenv

# 1
import discord
from discord.ext import commands

CHARACTER_LIMIT = 2000

intents = discord.Intents.default()
intents.members = True # see members of the server

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# 2
bot = commands.Bot(command_prefix='!', intents=intents)


async def send_message(ctx, response, reps):
   
    responses_per_message = CHARACTER_LIMIT // (len(response) + 1)
    messages = reps // responses_per_message

    for _ in range(messages):
        print(messages, responses_per_message)
        await ctx.send(' '.join([response for _ in range(responses_per_message)])) 

    await ctx.send(' '.join([response for _ in range(reps % responses_per_message)])) 


@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(f'{bot.user.name} has connected to Discord to {guild}')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name='quack', help='Responds with QUACK')
async def quack(ctx, reps: int):
    response = 'QUACK'
    await send_message(ctx, response, reps)

@bot.command(name='woof', help='Responds with WOOF')
async def woof(ctx, reps: int):
    response = 'WOOF'
    await send_message(ctx, response, reps)

@bot.command(name='quack_rep', help='QUACK with repetitions')
@commands.has_permissions(administrator=True)
async def quack_rep(ctx, reps: int):

    response = 'QUACK'




@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {member.guild.name}! Say "!quack" in Recruit\'s Pond to get some Quacks!'
    )

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

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

