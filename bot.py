import os
from dotenv import load_dotenv
import discord

bot = discord.Client(intents=discord.Intents.default())
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        # Print the server's ID and NAME.
        print(f"- {guild.id} (name: {guild.name})")
        
        #Increment the guild counter
        guild_count = guild_count + 1
        
    print("SampleDiscordBot is in " + str(guild_count) + "guilds")
    
@bot.event
async def on_message(message):
    if message.content == "Hello":
        await message.channel.send("Hello maidenless one!")
        
bot.run(DISCORD_TOKEN)

