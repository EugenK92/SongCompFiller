# bot.py
import os
import re
import discord
from dotenv import load_dotenv
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


async def read_latest_message(channel_name):
    # Fetch the channel by name
    channel = discord.utils.get(client.get_all_channels(), name=channel_name)

    if channel:
        # Fetch the channel's message history
        async for message in channel.history(limit=2):
            latest_message = message
        parsed_data = await parse_message_content(latest_message.content)
        await save_to_file(parsed_data)
        print("Done")
    else:
        print(f'Channel {channel_name} not found')

# Example usage
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself
    
    if message.content.startswith('!load'):
					 		link = message.content.split('!load')[1].strip()
					 		await save_link_to_file(link)
					 		await read_latest_message('testroom')

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