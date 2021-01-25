from util import load_conversation
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def create_chatbot() -> ChatBot:
        
    bot = ChatBot(
        'smol dom gf',
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        logic_adapters = [
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'bruh',
            }
        ],
        database_uri=None
    )

    trainer = ListTrainer(bot)

    paths = ('logs/0.json', 'logs/1.json', 'logs/2.json')
    convos = load_conversation(*paths)
    
    for convo in convos:
        trainer.train(convo)

    return bot


if __name__ == "__main__":
    bot = create_chatbot()

    print(bot.get_response(statement='hi'))
