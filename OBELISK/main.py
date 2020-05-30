import discord
import os
import json
import asyncio
import random

from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from asyncio import sleep
#Above are necessary imports to allow the bot to run properly.

def bot_prefix(bot, message):
	with open("prefixes.json", 'r') as f:
		prefixes = json.load(f)
	return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=bot_prefix)#Sets the bot's prefix
TOKEN = open("TOKEN.txt", "r").read()

@bot.event
async def on_guild_join(guild):
	with open("prefixes.json", 'r') as f:#Opens json file to read data from it
		prefixes = json.load(f)#Defines prefixes so when it is mentioned the json file is loaded
	prefixes[str(guild.id)] = 'ob!'#Default prefix for the bot
	with open("prefixes.json", 'w') as f:#Opens json file to write data to it
		json.dump(prefixes, f, indent=4)#Dumps prefix data into json file
	print(f"Joined {guild.name}. Prefix is set to {prefixes}.") #Prints when the prefix of the bot is changes in a server

@bot.event
async def on_guild_remove(guild):
	with open("prefixes.json", 'r') as f:#Opens json file to read data from it
		prefixes = json.load(f)
	prefixes.pop(str(guild.id))#Removes the prefix for the server the bot was removed from
	with open("prefixes.json", 'w') as f:#Opens json file to write data to it
		json.dump(prefixes, f, indent=4)#Dumps prefix data into json file
	print(f"Removed from {guild.name}. Prefix data removed from prefixes.json.")

@bot.command()
async def setprefix(ctx, prefix):
	await ctx.message.delete()
	with open("prefixes.json", 'r') as f:#Opens json file to read data from it
		prefixes = json.load(f)
	prefixes[str(ctx.guild.id)] = prefix
	with open("prefixes.json", 'w') as f:#Opens json file to write data to it
		json.dump(prefixes, f, indent=4)#Dumps prefix data into json file
	await ctx.send(f"New prefix set to `{prefix}`!")

for cog in os.listdir(".\\cogs"):#Looks for files in the cogs folder
	if cog.endswith(".py"):#Defines cog files as only those ending in ".py" or Python files
		try:
			cog = f"cogs.{cog.replace('.py', '')}"#Defines cog's name as the file name without the extension
			bot.load_extension(cog)#Loads the cog
			print(f"{cog} loaded.")#Prints in the console that the cog has been loaded. For logging purposes
		except Exception as e:
			print(f"{cog} could not load.")#Prints that the cog could not load
			raise e #Prevents bot startup

bot.run(TOKEN)