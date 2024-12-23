import discord
import os
import asyncio

TOKEN = "MTMyMDU0OTA5Nzg2MTgwODE3MA.GC2qIF.2V5jlLf52Mr2dGcQgm7FRiDb6gVNQgHMt6AmHw"  # Replace with your bot's token
IMAGE_DIR = "outputs/2404/20"  # Directory containing your images
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
CHANNEL_ID = 1320540944352809030  # Replace with your channel's ID
DELAY_BETWEEN_POSTS = 0.3  # Delay in seconds (300ms)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    
    for file_name in os.listdir(IMAGE_DIR):
        if os.path.splitext(file_name)[1].lower() in IMAGE_EXTENSIONS:
            try:
                await channel.send(file=discord.File(os.path.join(IMAGE_DIR, file_name)))
                print(f"Posted: {file_name}")
                await asyncio.sleep(DELAY_BETWEEN_POSTS)  # Wait before sending the next file
            except Exception as e:
                print(f"Error posting {file_name}: {e}")

    await client.close()

client.run(TOKEN)
