# discord.why
Just seeing how it would be to make an API wrapper for Discord.com :)

# Rate limiting
```
REST:
        POST Message |  5/5s     | per-channel
      DELETE Message |  5/1s     | per-channel
 PUT/DELETE Reaction |  300/300s | per-channel
        PATCH Member |  10/10s   | per-guild
   PATCH Member Nick |  1/1s     | per-guild
      PATCH Username |  2/3600s  | per-account
      |All Requests| |  50/1s    | per-account
      
WS:
     Gateway Connect |   1/5s    | per-account
     Presence Update |   5/60s   | per-session
   All Sent Messages | 120/60s   | per-session
```
