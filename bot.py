# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(f'{client.user.name} has connected to Discord to {guild}')
    members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')
    


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {member.guild.name}! Say "hi" in Recruit\'s Pond to get some Quacks!'
    )

@client.event
async def on_message(message):
    # ignore messages sent by this bot 
    if message.author == client.user:
        return 
    if 'hi' in message.content.lower():
        await message.channel.send("Quack")
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Exception message: {args[0]}\n')
        else:
            raise



client.run(TOKEN)