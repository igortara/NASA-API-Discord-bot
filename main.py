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
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
today = None


# -- NASA satelite image for today function --
@bot.tree.command(
    name="nasa_sat", description="Fetches the NASA satellite image for today."
)
async def nasa_sat(interaction: discord.Interaction):
    await interaction.response.defer()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    image_data = nasa_func.get_nasa_image(type="TrueColor")
    if image_data is None:
        await interaction.followup.send(
            "Sorry, I couldn't fetch the NASA satelite image for today."
        )
        return
    embded = discord.Embed(
        title="NASA Satelite Image",
        description=f"Here is the NASA satelite image for {today}!",
        color=0x0035A9,
    )
    embded.set_image(url="attachment://nasa_wallpaper.jpg")
    await interaction.followup.send(
        embed=embded, file=discord.File(fp=image_data, filename="nasa_wallpaper.jpg")
    )


# -- NASA FIRMS image for today function --
@bot.tree.command(name="fires", description="Fetches the NASA FIRMS image for today.")
async def fires(interaction: discord.Interaction):
    await interaction.response.defer()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    image_data = nasa_func.get_nasa_image(type="FIRMS")
    if image_data is None:
        await interaction.response.send_message(
            "Sorry, I couldn't fetch the NASA FIRMS image for today."
        )
        return
    embded = discord.Embed(
        title="NASA FIRMS Image",
        description=f"Here is the NASA FIRMS image for {today}!",
        color=0x0035A9,
    )
    embded.set_image(url="attachment://nasa_wallpaper.jpg")
    await interaction.followup.send(
        embed=embded, file=discord.File(fp=image_data, filename="nasa_wallpaper.jpg")
    )


# -- Help function --
@bot.tree.command(name="helpme", description="Displays help information.")
async def helpme(interaction: discord.Interaction):
    help_text = """
    **!nasa_sat** - Fetches the NASA satellite image for today.
    **!fires** - Fetches the NASA FIRMS image for today.
    **!apod** - Fetches the Astronomy Picture of the Day (APOD) image for today.
    **!helpme** - Displays this help message.
    """
    await interaction.response.send_message(help_text)


# -- NASA APOD image for today function --
@bot.tree.command(
    name="apod",
    description="Fetches the Astronomy Picture of the Day (APOD) image for today.",
)
async def apod(interaction: discord.Interaction):
    embed = discord.Embed(
        title="NASA APOD",
        description="Here is today's Astronomy Picture of the Day (APOD)!",
        color=0x0035A9,
    )
    image_url = nasa_func.get_apod_image()
    if image_url is not None:
        embed.set_image(url=image_url)
        await interaction.followup.send(embed=embed)
    else:
        await interaction.followup.send(
            "Sorry, I couldn't fetch the APOD image for today."
        )




@bot.tree.command(name="ping", description="Checks if the bot is responsive.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.tree.sync()


# -- Run the bot --
if __name__ == "__main__":
    bot.run(BOT_TOKEN)
