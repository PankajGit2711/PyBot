from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

def training():
    bot = ChatBot('Bot')
    trainer = ListTrainer(bot)

    corpus_path = 'C:/Users/Pankaj Sharma/Downloads/Compressed/chatterbot-corpus-master/chatterbot_corpus/data/'

    for files in os.listdir(corpus_path):
        trainer.train(corpus_path + files)
    print("Training Completed")
   
training()
