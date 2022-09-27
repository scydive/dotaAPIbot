import discord
from discord.ext import commands
import requests
import json

TOKEN = 'discord bot token'
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)



@client.event
async def on_ready():
    response = requests.get('https://api.opendota.com/api/players/playerid/wl')
    print('h')
    with open('loss.txt') as f:
        contents = int(f.readlines()[0])
    lose_val = response.json()['lose']
    if contents < lose_val:
        previous_val = lose_val
        lose_val = str(lose_val)
        with open('loss.txt', 'w') as f:
            f.write(lose_val)
        channel= client.get_channel('channel id')
        await channel.send(f'Loss registered. Current number is: {lose_val}')

client.run(TOKEN)








