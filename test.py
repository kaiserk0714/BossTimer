import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Login")
    print(client.user.name)
    print(client.user.id)
    print("-----------------------------------")
    await client.change_presence(game=discord.Game(name='', type=1))
    
@client.event
async def on_message(message):
    if message.content.startswith("hi"):
        await client.send_message(message.channel, "HI")
        
access_token = os.environ["BOT_TOKEN"]
client.run("NjU5NzEzMDgyOTAxMTM1MzYw.XhmgiQ.T2S8vaoTmnMpVvFy_MV3vo966Jo")
