# SongCompFiller

- Check current Chrome Version 
- Download Driver [here](https://googlechromelabs.github.io/chrome-for-testing/#stable)

```
wget <link>
```

- Move the downloaded chromedriver executable to a directory that is already in your system's PATH. Common locations include /usr/local/bin 

- Create a Discord Bot like this [here](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)
- Set Permissions: permissions=76800 scope=bot
- Add Bot to own Discord

- Create Channel for SongComp Links

- Create .env file in project directory
```
# .env
DISCORD_TOKEN="<insert token here>"
DISCORD_ALLOW_ROLE="<Role>"

```

Run Discordbot:
```
python3 discordbot.py
```

- Type into Channel
```
!load <SongCompLink here> <discord message link>

!load link.com https://discord.com/channels/123/456/789


If Terminal tells "Done" 

Load Songs into SongComp
```
python3 insert.py
```

- Songlist in Channel should have this structure
```
The Black Eyed Peas - Where Is The Love? | https://www.youtube.com/watch?v=WpYeekQkAdc
Eminem - Mockingbird | https://www.youtube.com/watch?v=S9bCLPwzSC0 | 00:07
```

If no timestamp is set then it will be 00:00