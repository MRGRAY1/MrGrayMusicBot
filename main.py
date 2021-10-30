import discord
import os
from dotenv import load_dotenv

async def get_cmd(message, user):
    await message.channel.send("This is a test")

load_dotenv(".env")
client = discord.Client()
botkey = os.getenv("BOTKEY")
print (botkey)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    user = message.author.nick
    if user == None:
        user = message.author.name
    if message.author == client.user:
        return
    elif message.content.startswith("."):
        #await message.channel.send(get_cmd(message, user))
        await get_cmd(message, user)

client.run(botkey)