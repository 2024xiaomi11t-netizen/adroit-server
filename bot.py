import discord

# Discord bot token
DISCORD_BOT_TOKEN = "MTUwMDU1MDAwOTQ2NzQ0NDEzMTQ.GckSZx.skuihSv2Qsj2sxtUJzhUywGWNTuVAYeFaB4814"
DISCORD_CHANNEL_ID = 1496248008961032367

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot hazırdır: {client.user}")

@client.event
async def on_message(message):
    if message.channel.id == DISCORD_CHANNEL_ID and message.content == "!bax":
        print("!bax əmri alındı!")
        # FCM göndərmə deaktiv
        # await send_fcm_notification()

client.run(DISCORD_BOT_TOKEN)
