from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot("chatbot", read_only=False, logic_adpaters=["chatterbot.logic.BestMatch"])

list_to_train = [
               "hi",
               "hi there",
               "what's your name?",
               "I'm a chatbot"
               "how old are you?"
               "I'm ageless!"
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)
