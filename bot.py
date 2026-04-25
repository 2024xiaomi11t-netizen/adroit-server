import discord
import asyncio
import httpx
import json
import google.auth.transport.requests
from google.oauth2 import service_account

# Discord bot token
DISCORD_BOT_TOKEN = "MTQ5NjI0Mjg0OTg3NDg0MTYzMA.G_1ai7.ucX7THFSKdC80EsQiTAoAv2623XD0rybZc-MYU"
DISCORD_CHANNEL_ID = 1496248008961032367

# FCM
FCM_TOKEN = "eFFdIA2dSve6ziGLzOr5IP:APA91bG1u8d2xjDmAWasIceGHhaEDo1jeWwR47BHssNKsyCtSs5eVHbeJjKuxC7piM3RuhR-9XLbKbzWc415PKy2oN5U3Zk_ARk5Tz0py8lJid_KZdxJywI"
SERVICE_ACCOUNT_FILE = "service-account.json"
PROJECT_ID = "evlad-8a004"

async def send_fcm_notification():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/firebase.messaging"]
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    access_token = credentials.token

    url = f"https://fcm.googleapis.com/v1/projects/{PROJECT_ID}/messages:send"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": {
            "token": FCM_TOKEN,
            "data": {
                "command": "bax"
            }
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        print(f"FCM cavab: {response.status_code} - {response.text}")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot hazırdır: {client.user}")

@client.event
async def on_message(message):
    if message.channel.id == DISCORD_CHANNEL_ID and message.content == "!bax":
        print("!bax əmri alındı, FCM göndərilir...")
        await send_fcm_notification()

client.run(DISCORD_BOT_TOKEN)