# discord.why
A python Discord wrapper made in well, python.

Made to be used by devs who want something a bit more, general.

# Basic Examples
### Sending a message
```python
import discordwhy

Discord = Discord(token)

content = Discord.send_message(
    channel = 894348837009915935,
    message = 'Sent via discord.why'
).response

print(content)
```

Output: `Sent: True; Status: 200`

### Getting user details
```python
import discordwhy

Discord = Discord(token)

content = Discord.get_user(
    user = 894348837009915935,
).response

print(content)
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
