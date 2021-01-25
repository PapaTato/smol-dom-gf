from discord.ext.commands import Bot
import json
import logging

from typing import List


async def archive_channel(bot : Bot, id : int):
    print(f'saving channel with id {id}')
    channel : discord.TextChannel = bot.get_channel(id)
    path = f'{channel.name}{id}.json' 
    
    messages : List[discord.Message] = await channel.history(limit=None).flatten()
    output = [
        {
            'author': message.author.id,
            'content': message.content
        }
        for message in messages[::-1]
    ]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(output, f)

    print(f'saved {channel.name} texts')


def load_conversation(*paths : str) -> List[List[str]]:
    """loads json files of convos in order and then outputs list containing all convos"""
    CONVO_LENGTH = 10
    conversations = []
    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            conversation : List = json.load(f)
            logging.info(f'loaded {len(conversation)}, adding to total.')
            conversations += [message.get('content') for message in conversation]

    all_convos = [conversations[i:i + CONVO_LENGTH] for i in range(0, len(conversations) - CONVO_LENGTH, CONVO_LENGTH)]
    return list(filter(lambda x: len(x) == CONVO_LENGTH, all_convos))


if __name__ == "__main__":
    paths = ('logs/0.json', 'logs/1.json', 'logs/2.json')
    convos = load_conversation(*paths)

    print(len(convos))

    # py -m pip install chatterbot

