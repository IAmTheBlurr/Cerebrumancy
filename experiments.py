""" This file is used to test the functionality of the ChatGPT class. """
from configuration import Configuration
from entities import Assistant, Chat, System, User


# create a configuration object
config = Configuration('config.json')


if __name__ == '__main__':
    messages = [
        System("You are a helpful, pattern-following assistant."),
        User("Help me translate the following corporate jargon into plain English."),
        Assistant("Sure, I'd be happy to!"),
        User("New synergies will help drive top-line growth."),
        Assistant("Things working well together will increase revenue."),
        User("Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage."),
        Assistant("Let's talk later when we're less busy about how to do better."),
        User("This late pivot means we don't have time to boil the ocean for the client deliverable.")
    ]

    chat = Chat(config, messages)

    chat.create()
    # Response is correctly "We don't have enough time to complete everything perfectly for the client."
