import random
import yaml
import re
import discord
import asyncio

def load_yaml(path : str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


CONFIG : dict = load_yaml('config.yaml')
MEMBERS : dict = load_yaml('members.yaml')



def check_whois(content : str) -> bool:
    triggers = r'who.*s?'
    return bool(re.search(triggers, content))


def check_greetings(content : str) -> bool:
    triggers = [r'hi+', r'he+y+', r'h+e+l+o', r'good ?morning', r'good ?night', r'gluten', r'hai']
    return any(re.search(trigger, content) for trigger in triggers)


async def whois(message : discord.Message):
    await message.channel.send('your mom')

async def greetings(message : discord.Message):
    channel : discord.TextChannel = message.channel
    user_id = message.author.id
    nicknames = MEMBERS.get(f'{user_id}')
    nickname = random.choice(nicknames) if nicknames else 'weirdo'

    await channel.trigger_typing()
    await asyncio.sleep(random.randint(1, 5))

    await message.channel.send(f'hey {nickname}')

# ordered by importance of check
EVENT_TYPE = {
    check_whois: whois,
    check_greetings: greetings,
}

async def handle_message(message : discord.Message):
    engage = CONFIG['care_perc']
    if engage <= random.randint(0, 100):
        return

    content = message.content
    for key, value in EVENT_TYPE.items():
        if key(content):
            await value(message)
            break

async def handle_mention(message : discord.Message):
    channel : discord.TextChannel = message.channel
    user_id : discord.Member = message.author.id
    nicknames = MEMBERS.get(f'{user_id}')
    nickname = random.choice(nicknames) if nicknames else 'weirdo'

    reply = random.choice(['what', f'what do you want {nickname}?', 'why tag', 'no'])
    await asyncio.sleep(random.randint(3, 10))
    await channel.trigger_typing()
    await asyncio.sleep(random.randint(7, 10))
    await channel.send(reply)

