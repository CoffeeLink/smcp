#Importing Packages
import asyncio
import discord
intents = discord.Intents.default()
intents.members = True
import json

import time
import os
import sys

from discord.ext import commands, tasks
from datetime import datetime, timedelta



async def get_prefix(bot, message):
    prefix = ["smcp ", "Smcp "]
    return commands.when_mentioned_or(*prefix)(bot, message)

#Defining bot
bot = commands.Bot(command_prefix=get_prefix, description='Helper Bot', intents=intents)
bot.remove_command('help')

cogs = ['']

for f in cogs:
    bot.load_extension(f'lib.cogs.{f}')
    print(f'Loaded {f} cog')

with open("lib/json/config.json", "r") as f:
    config = json.load(f)
TOKEN = config['token']
bot.run(TOKEN)