# discord.why
A python Discord wrapper made in well, python.

Made to be used by devs who want something a bit more, general.

# Basic Examples
### Sending a message

Send a message with the content *'testing discord.why'*, after the message is sent delete after 10 seconds.

```python
from wrapper import *

Discord = Discord('TOKEN')

content = Discord.send_message(
    channel = 904513273058177055,
    message = 'testing discord.why',
    delete_after = 10
).json()

print(content)
```

Output: `Sent: True; Status: 200`

### Getting user details
```python
from wrapper import *

Discord = Discord('TOKEN')

content = Discord.get_user(
    user = 894348837009915935,
).json()

print(content)
```

### Multiple token reactions
```python
from wrapper import *

def send(w):
    content = w.create_reaction(
        channel = 904627884944138240,
        message = 904634461356965888,
        reaction = 'cool'
    ).json()
    
    print(content)

for token in open('tokens.txt', 'r').readlines():
    Wrapper = Discord(token.rstrip())
    send(Wrapper)
```


Output: `Status: 200`

# Basics

### Rate Limiting: REST

| Rest Type     | API Location  | Limit         |
| ------------- | ------------- | ------------- |
| POST Message  | Per-Channel  | 5/5s              |
| DELETE Message| Per-Channel  | 5/1s           |
| PUT/DELETE Reaction  | Per-Channel  | 300/300s              |
| PATCH Member | Per-Guild  |  10/10s             |
| PATCH Member Nick | Per-Guild  |  1/1s             |
| PATCH Username | Per-Account  | 2/3600s
| All Requests  | Per-Account  |  50/1s             |


### Rate Limiting: WS

| Rest Type     | API Location  | Limit         |
| ------------- | ------------- | ------------- |
|     Gateway Connect |   Per-Account    | 1/5s
|     Presence Update |   Per-Session  | 5/60s
|   All Sent Messages | Per-Session   | 120/60s
