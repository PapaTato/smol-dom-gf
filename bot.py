import discord
import asyncio
import logging
import json

from discord.ext.commands import Bot, Context
from events import handle_mention, handle_message
from typing import List
from chatbot import create_chatbot

intents = discord.Intents.default()
intents.members = True


logging.getLogger().setLevel(logging.INFO)

chat_bot = create_chatbot()
bot = Bot('-', intents=intents)


@bot.event
async def on_ready():
    print(f'connected with user {bot.user}')
    
CHANNEL_ID = 0 # discord channel where the bot replies

@bot.event
async def on_message(message : discord.Message):
    if message.author == bot.user:
        return

    channel : discord.TextChannel = message.channel
    if channel.id == CHANNEL_ID:
        await channel.trigger_typing()
        if not message.content:
            return 'what'
        response = chat_bot.get_response(statement=message.content)
        await channel.send(response if response else 'bruh')

    return

    if bot.user in message.mentions:
        await handle_mention(message)
    else:
        await handle_message(message)

if __name__=='__main__':
   bot.run("token")
