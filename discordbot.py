# bot.py
import os
import re
import discord
from dotenv import load_dotenv
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_ALLOW_ROLE = os.getenv('DISCORD_ALLOW_ROLE')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Example usage
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself
    
    role = discord.utils.get(message.author.roles, name=DISCORD_ALLOW_ROLE)
    if role:
      if message.content.startswith('!load'):
					 		link = message.content.split(' ')[1].strip()
					 		await save_link_to_file(link)

					 		messageLink = message.content.split(' ')[2].strip()
					 		songNames = await getMessage(messageLink)
					 		parsed_data = await parse_message_content(songNames)
					 		await save_to_file(parsed_data)
					 		print("Done")

async def getMessage(link):
    if "https://discord.com/channels/" in link:
        link_parts = link.split('/')
        guild_id = int(link_parts[4])
        channel_id = int(link_parts[5])
        message_id = int(link_parts[6])

        try:
            # Fetch the message using the extracted IDs
            guild = discord.utils.get(client.guilds, id=guild_id)
            channel = discord.utils.get(guild.channels, id=channel_id)
            fetched_message = await channel.fetch_message(message_id)

            if "Kategorie" in fetched_message.content:
              fetched_message.content = await removeFirstLine(fetched_message.content)

            return fetched_message.content
        except discord.NotFound:
            print("Message not found.")

async def removeFirstLine(text):
  blocks = [block.strip() for block in text.strip().split('\n\n')]
  modified_blocks = [block.split('\n', 1)[1] if '\n' in block else '' for block in blocks]
  result = '\n\n'.join(modified_blocks)

  return result

async def parse_message_content(content):
    lines = content.split('\n')

    result = []

    for line in lines:
        parts = line.split('|')
        identifier = parts[0].strip() if parts else ""
        name = parts[2].strip() if len(parts) > 2 else "00:00"
        link = parts[1].strip() if len(parts) > 1 else ""

        result.append({"name": name, "link": link})

    return result

async def save_link_to_file(link, file_path='link.txt'):
    with open(file_path, 'w') as file:
        file.write(link)

async def save_to_file(data, file_path='output.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

client.run(TOKEN)