import discord
import os
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content == "$regras":
            await message.server.send(f'{message.author.name}, as regras são:{os.linesep} ')

client = MyClient()
client.run('') #here too my son