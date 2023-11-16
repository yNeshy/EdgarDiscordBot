# bot.py
import os

import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
from memory import FilingsMemory
from edgar import Crawler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
channel = None

class EdgarListener(commands.Cog):
    def __init__(self, channel):
        self.index = 0
        self.channel = channel

    def cog_unload(self):
        self.edgar_loop.cancel()

    def start(self):
        self.edgar_loop.start()

    @tasks.loop(seconds=5)
    async def edgar_loop(self):
        memory = FilingsMemory()
        crawler = Crawler()

        filings = await crawler.fetch_hits()
        for filing in filings :
            if not memory.exists(filing):
                await channel.send("new filing found: "+ str(filing))
                await memory.insert(filing)

        if len(filings) == 0:
            await channel.send("we have been banned. Sleeping 15 seconds.")
            
        await crawler.reset()




@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$boot'):
        channel = message.channel
        task = EdgarListener(channel)

        task.start()


# class KyleBot(discord.Client):
    
#     async def on_ready(self):
#         print(f'We have logged in as {self.user}')

#     async def on_message(self, message):
#         if message.author == self.user:
#             return

#         if message.content.startswith('$hello'):
#             await message.channel.send('Hello!')

#         if message.content.startswith('$boot'):
#             task_loop.start() # important to start the loop



client.run(TOKEN)
