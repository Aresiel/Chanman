import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!!")




@client.event
async def on_ready():
    print ("Bot is ready!")
    await client.change_presence(game=discord.Game(name='discord.py'))


@client.event
async def on_message(message):
    if message.content.startswith('!!ping'):
        userId = message.author.id
        await client.send_message(message.channel, "<@" + userId + ">" + " Pong!")
        print (userId + " used ping command")

    if message.content.startswith('!!say'):
        userId = message.author.id
        args = message.content.split(" ")
        await client.send_message(message.channel, "<@" + userId + ">" + " told me to say: " + "%s" % (" ".join(args[1:])))
        print (userId + " used say command")

    if message.content.startswith('!!beste'):
        userId = message.author.id
        await client.send_message(message.channel, "<@185856049880891394> is the best in the world!!!")
        print (userId + " used elias is best command")

    if message.content.startswith('!!terminate'):
        if message.author.id == ("104933285506908160"):
            await client.send_message(message.channel, "Bot terminated by GP")
            print ("Bot terminated by GP")
            exit()
        else:
            await client.send_message(message.channel, "Ya didn't think that'd work, did ya?")
            print (userId + " tried to use terminate")

    if message.content.startswith('!!admin?'):
        if "432453583959621634" in [role.id for role in message.author.roles]:
            userId = message.author.id
            await client.send_message(message.channel, "<@" + userId + "> Yes, you are an admin!")
            print(userId + " used admin? command")
        else:
            userId = message.author.id
            await client.send_message(message.channel, "<@" + userId + "> Nah, you ain't an admin!")
            print(userId + " tried to use admin? command")

    if "python sucks" in message.content.lower():
        userId = message.author.id
        await client.delete_message(message)
        await client.send_message(message.channel, "**I DO NOT SUCK!!!**")
        await asyncio.sleep(2)
        await client.kick(message.author)
        await client.send_typing(message.channel)
        await asyncio.sleep(4)
        await client.send_message(message.channel, "Ehm.... I might've *accidentally* kicked <@" + userId + "> for saying that I suck....")
        print(userId + "said that I sucked...")

    if "minecraft sucks" in message.content.lower():
        userId = message.author.id
        await asyncio.sleep(1)
        await client.delete_message(message)
        await client.send_message(message.channel, "What was that?")

    if message.content.startswith('!!cm'):
        if message.author.id == ("104933285506908160"):
            msg = input('Message: ')
            chn = client.get_channel(input('Channel: '))
            await client.send_message(chn, msg)
            await client.delete_message(message)
        else:
            await client.send_message(message.channel, "Sry, only works for GP")

    if message.content.startswith('!!qm'):
        if message.author.id == ("104933285506908160"):
            await client.delete_message(message)
            msg = input('Message: ')
            await client.send_message(message.channel, msg)
        else:
            await client.send_message(message.channel, "Sry, only works for GP")









client.run("NDMyMjYzNTg1MzU2NDQ3NzY0.Daqy4w.RlAaoEfk04sR9aNy_JClLWShdbE")
