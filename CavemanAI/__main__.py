import asyncio
import ollama
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(
        command_prefix=commands.when_mentioned_or('='), 
        intents=intents)

async def ask_bot(ctx, prompt):

    print(prompt)

    message = {
        'role':'user',
        'content': prompt,
    }

    response = ollama.chat(
        model = 'caveman',
        stream = False,
        messages = [message]
    )
    message_back = response['message']['content']
    print(message_back)
    await ctx.send(content=message_back)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.event
async def on_message(message):
    command_prefix = '='
    if not message.content.startswith(command_prefix + 'grug'):
        return

    print('got message')

    ctx = await client.get_context(message)
    await ask_bot(ctx, message.content)

async def main():
    token = await get_token()
    async with client:
        await client.start(token)

async def get_token():
    token = ''
    with open('discord.token', 'r') as f:
        token = f.read()
    print(f'token: {token}')
    return token

asyncio.run(main())
