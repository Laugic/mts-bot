# bot.py
import os
import json
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
cirno_data = None
prefix = '!'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print('Loading mod data')
    load_data(cirno_data, 'cirno')
    
def load_data(data_field, mod_id):
    with open(f'data/{mod_id}/items.json') as json_file:
        data_field = json.load(json_file)
    print(f'Loaded {mod_id}!')

def is_command(message):
    return message.content.startswith(prefix)

def del_char

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if is_command(message):
        
client.run(token)
