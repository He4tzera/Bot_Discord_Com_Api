
import discord
import requests
import json
from HLTV import *
from bs4 import BeautifulSoup

data_json = requests.get("https://hltv-api.vercel.app/api/teams.json")
jsonDados = data_json.content
dados = json.loads(jsonDados)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!Top1':
            await message.channel.send(dados['name'])
            await message.channel.send(dados['logo'])
            await message.channel.send(f"Coach: {dados['coach']}")
            for item in dados['players']:
                await message.channel.send(item['fullname']) and await message.channel.send(item["image"])



intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

client = MyClient(intents=intents)
client.run('Token')
