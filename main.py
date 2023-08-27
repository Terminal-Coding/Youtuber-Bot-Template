import discord
import requests
from bs4 import BeautifulSoup

# Initialize Discord intents
intents = discord.Intents.all()
# Create a Discord client with the initialized intents
client = discord.Client(intents=intents)

# Event triggered when the bot is ready and connected to Discord
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event triggered when a message is sent in a channel the bot has access to
@client.event
async def on_message(message):
    # Check if the message content starts with '?commands'
    if message.content.startswith('?commands'):
        # Create an embedded message for the list of commands
        embedVar = discord.Embed(title="Here is a list of my commands!", color=0x00ff00)
        embedVar.add_field(name="?commands", value="Shows a list of commands.", inline=False)
        embedVar.add_field(name="?help", value="Helps you navigate the discord.", inline=False)
        embedVar.add_field(name="?sub count", value="Gives [CHANNELS NAME] current subcount.", inline=False)
        embedVar.add_field(name="?member count", value="Give [CHANNELS NAME] current discord server member count.")
        # Send the embedded message to the same channel
        await message.channel.send(embed=embedVar)

    elif message.content.startswith('?help'):
        # Create an embedded message for the welcome message and instructions
        embedVar = discord.Embed(title="Welcome To The [DISCORDS NAME] Discord!", color=0x00ff00)
        embedVar.add_field(name="Want to have a chat with someone in our community?", value="Check out general",
                           inline=False)
        embedVar.add_field(name="[EXTRAS]", value="Then go to #︱faq", inline=False)
        embedVar.add_field(name="Want to open a support ticket?", value="Then just head over to support.",
                           inline=False)
        embedVar.add_field(name="Enjoy!", value="", inline=False)
        # Send the embedded message to the same channel
        await message.channel.send(embed=embedVar)

    elif message.content.startswith('?sub count'):
        # Retrieve subscriber count from a YouTube channel's HTML page
        url = 'https://www.youtube.com/@[CHANNELS NAME]'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        dat = str(soup)
        l = dat.partition("subscribers")
        sub = l[0][len(l[0]) - 22:]
        txt = sub.split(':')[2]
        txt = txt.replace('"', "")
        epicman2389subs = (txt)
        # Create an embedded message for the subscriber count
        embedVar = discord.Embed(title="Here is [CHANNELS NAME] subscriber count!", color=0x00ff00)
        embedVar.add_field(name=epicman2389subs, value="", inline=False)
        # Send the embedded message to the same channel
        await message.channel.send(embed=embedVar)

    elif message.content == '?member count':
        # Retrieve the member count of the Discord server
        member_count = len(message.guild.members)
        # Create an embedded message for the member count
        embedVar = discord.Embed(title="Here is [DISCORDS NAME] discord server member count!", color=0x00ff00)
        embedVar.add_field(name=member_count, value="", inline=False)
        # Send the embedded message to the same channel
        await message.channel.send(embed=embedVar)

# Run the bot using the provided bot token
client.run('[BOT TOKEN]')
