import discord
import json

from discord.ext import commands

class Events(commands.Cog):#Sets a class for the cog
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("----------")
		print("Logged in as")
		print(self.bot.user.name)
		print("----------")

def setup(bot):#Defines the statup sequence for the cog
	bot.add_cog(Events(bot))#Starts the cog, making it accessible to the rest of the bot's files.