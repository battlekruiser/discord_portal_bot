import discord
import sys
import random
import requests
import re

exp_name = re.compile('(?<=[1-9]\/)(.*)(?=\?)')
exp_channel = re.compile('\<\#+[\d]+\>')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {}'.format(self.user))
        print('the encoding is {}'.format(sys.stdout.encoding))
        
    async def on_message(self, message):
        #print('{}@{}: {}'.format(message.author, message.channel, message.content))
        
        if('portal' in message.content.lower()
           or 'портал' in message.content.lower()
          ): 
            #await message.channel.send(exp_hi.findall(message.content))
            if len(exp_channel.findall(message.content)) > 0:
                channel_id = exp_channel.findall(message.content)[0][2:-1]
                channel =  message.channel.guild.get_channel_or_thread(int(channel_id))
                #print(channel_id,type(channel_id), channel)
                gateback = await channel.send(message.jump_url)
                await message.reply(gateback.jump_url)
            
intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents = intents)
token = None
with open('token') as f:
    token = f.readline()
client.run(token)

#todo bump reminder, poggle capitalisation tracker, uhhhhhhh
#todo if the portal ask is a reply to a message, quote that message in the target channel