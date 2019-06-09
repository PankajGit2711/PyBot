from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.adapters import Adapter
import os
import logging

def startchat(message):
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)

    bot = ChatBot('Bot',
                      storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
               logic_adapters = [
                   {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.90
                   }
                ],   
            trainer = 'chatterbot.trainers.ListTrainer')
    trainer = ListTrainer(bot)
    while True:
        if message.strip() != 'Bye':
            result = bot.get_response(message)
            reply = str(result)
            return reply
        if message.strip() == 'Bye':
            return 'Bye'
            break


