import os
import random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    waste_input = message.content.lower()

    if 'plastik' in waste_input:
        await message.channel.send('Bu bir plastik atık geri dönüşüm kutularına atabilirsin')
    if 'kağıt' in waste_input:
        await message.channel.send('Bu bir kağıt atık geri dönüşüm kutularına atabilirsin')
    if 'pil' in waste_input:
        await message.channel.send('Bu bir pil okullarda ve bazı alışveris merkezlerinde pil kutuları bulunur onlara atabilirsin')
    if 'metal' in waste_input:
        await message.channel.send('Bu bir metal atık geri dönüşüm kutularına atabilirsin')
    else:
        await message.channel.send('Bu bir diğer atık türü normal çöpe atabilirsin')


bot.run("TOKEN")

