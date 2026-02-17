# -- NASA API Bot by Feliks --
# ----------------------------
# -- Imports --
import nasa_func
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
load_dotenv()
# -- Init --
apod_url = "https://apod.nasa.gov/apod/astropix.html"
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
today = None
# -- NASA satelite image for today function --
@bot.command(name="nasa_sat", description="Fetches the NASA satellite image for today.")
async def nasa_sat(ctx):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    image_url = nasa_func.get_nasa_image(type="TrueColor")
    if image_url is None:
        await ctx.send("Sorry, I couldn't fetch the NASA satelite image for today.")
        return
    embded = discord.Embed(title="NASA Satelite Image", description=f"Here is the NASA satelite image for {today}!", color=0x0035a9)
    embded.set_image(url="attachment://nasa_wallpaper.jpg")
    await ctx.send(embed=embded , file=discord.File(image_url))
    os.remove("nasa_wallpaper.jpg")
# -- NASA FIRMS image for today function --
@bot.command(name="fires", description="Fetches the NASA FIRMS image for today.")
async def fires(ctx):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    image_url = nasa_func.get_nasa_image(type="FIRMS")
    if image_url is None:
        await ctx.send("Sorry, I couldn't fetch the NASA FIRMS image for today.")
        return
    embded = discord.Embed(title="NASA FIRMS Image", description=f"Here is the NASA FIRMS image for {today}!", color=0x0035a9)
    embded.set_image(url="attachment://nasa_wallpaper.jpg")
    await ctx.send(embed=embded , file=discord.File(image_url))
    os.remove("nasa_wallpaper.jpg")   
# -- Help function --
@bot.command(name="helpme", description="Displays help information.")
async def helpme(ctx):
    help_text = """
    **!nasa_sat** - Fetches the NASA satellite image for today.
    **!fires** - Fetches the NASA FIRMS image for today.
    **!apod** - Fetches the Astronomy Picture of the Day (APOD) image for today.
    **!helpme** - Displays this help message.
    """
    await ctx.send(help_text)
# -- NASA APOD image for today function --
@bot.command(name="apod", description="Fetches the Astronomy Picture of the Day (APOD) image for today.")
async def apod(ctx):
    embed = discord.Embed(title="NASA APOD", description="Here is today's Astronomy Picture of the Day (APOD)!", color=0x0035a9)
    image_url = nasa_func.get_apod_image()
    if image_url is not None:
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)
@bot.command(name="ping", description="Checks if the bot is responsive.")
async def ping(ctx):
    await ctx.send("Pong🏓!")
# -- Run the bot --
if __name__ == "__main__":
    bot.run(BOT_TOKEN)