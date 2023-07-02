# Cerebrumancy
The Animation of the Mind &amp;&amp; OpenAI

    All great advances in technology involve a better human-machine interface, 
    conecting us more intimately to our machines.
    
    - Walter Isaacson
      Twitter Spaces, June 13th 2023


## Motivations
To wrap the OpenAI Python API client library in a more object-oriented way that is easier to use, more scalable, more intuitive, requiring less input, and hopefully more fun to use.

## Installation
### Coming Soon (not available on PyPI yet)

## Design Philosophy
The OpenAI Python API client library is a great tool for interacting with the OpenAI API. However, the library has a sort of "raw data" design to it, designed by data scientists if you go by the code examples provided at https://github.com/openai/openai-cookbook

Under the hood, Cerebrumancy uses all the same functions and functionality as the OpenAI Python library, but it wraps them "entity" classes meant to encourage sharable modularity.

## Before & After

### Before (The Raw OpenAI Way)
```python
import openai

openai.api_key = 'YOUR_API_KEY'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful, pattern-following assistant."},
        {"role": "user", "name": "Bob", "content": "Help me translate the following corporate jargon into plain English."},
        {"role": "assistant", "content": "Sure, I'd be happy to!"},
        {"role": "user", "name": "Bob",  "content": "New synergies will help drive top-line growth."},
        {"role": "assistant", "content": "Things working well together will increase revenue."},
        {"role": "user", "name": "Bob",  "content": "Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage."},
        {"role": "assistant", "content": "Let's talk later when we're less busy about how to do better."},
        {"role": "user", "name": "Bob",  "content": "This late pivot means we don't have time to boil the ocean for the client deliverable."},
    ],
    temperature=0,
)

print(response["choices"][0]["message"]["content"])
```

### After (The Cerebrumancy Way)

```python
from cerebrumancy.core import Config
from cerebrumancy.gpt_entities import Assistant, Chat, System, User

config = Config("config.json")

chat = Chat(config)

system = System("You are a helpful, pattern-following assistant.")
chat.add_system(system)

assistant = Assistant()
bob = User("Bob")

chat.add_messages([
    bob("Help me translate the following corporate jargon into plain English."),
    assistant("Sure, I'd be happy to!"),
    bob('New synergies will help drive top-line growth.'),
    assistant('Things working well together will increase revenue.'),
    bob("Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage."),
    assistant("Let's talk later when we're less busy about how to do better."),
    bob("This late pivot means we don't have time to boil the ocean for the client deliverable."),
])

bob.say("This late pivot means we don't have time to boil the ocean for the client deliverable.")

chat.print_latest()
```

In the example above, the `bob` object is automatically associated to the `chat` object, so when we called `bob.say("...")`, the message was automatically added to the messages list stored in `chat` when the chat completion is called under the hood.

## Consider This...
If you stuck with the old way, how would you handle a situation where you wanted to start multiple worker chat instances?

How would you handle a situation where you wanted to have multiple chat instances with different configurations?

In our "After" example, we can have multiple Chat instances with their own configurations, their own message histories, and each of them could be running in separate worker instances, threads, or processes.

In our "After" example, we can have multiple User instances, each with their own name, and each with their own message history as well.

Those User instances can be passed into and made a part of multiple Chat instances.

We can define multiple different types of "systems" in advance of and outside of Chat instances.

None of this is possible with the "Before" example.  It would be very difficult to scale the "Before" example to handle multiple chat instances, multiple users, and multiple system types, especially if you wanted to run them in separate worker instances, threads, or processes.

## Why Care?
### Game Development
Let's say you wanted to create a game where there were multiple characters, each with their own distinct personalities, and you wanted to have them interact with each other in a way that was believable and fun.

You would want to maintain a sense of persistence of data for each character, their personality types, their chat history with various player characters, perhaps.

With the `Chat` class, you can do that a lot more readily and with fewer system inputs than would be possible with the "Before" example.

### Software Development
Let's say you're working on a project and there happen to be 10 module files at the time.

You could create 10 `Chat` instances in parallel for each of the 10 files, each instance producing its own tests, suggestions for improvement, and documentation.

## Examples
### Coming Soon