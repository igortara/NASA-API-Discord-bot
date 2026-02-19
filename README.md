# NASA Discord Bot

A small Discord bot that fetches daily NASA images (satellite imagery and APOD) and posts them to a channel.

**Features**
- Fetch satellite TrueColor images (`!nasa_sat`).
- Fetch FIRMS thermal anomaly images (`!fires`).
- Fetch Astronomy Picture of the Day (`!apod`).
- Simple help command (`!helpme`).

**Requirements**
- Python 3.10+ (tested on 3.12)
- A Discord bot token and a server where the bot has been invited.

**Dependencies**
- discord.py
- python-dotenv
- requests
- beautifulsoup4

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

**Setup (.env)**
The repository ignores the `.env` file. You must create it yourself in the project root with your bot token:

```
BOT_TOKEN=your_discord_bot_token_here
```

Ensure you keep this file private and do not commit it to version control.

**Running the bot**
1. Create the `.env` file as above.
2. (Optional) Verify your bot has the required intents enabled in the Discord Developer Portal if you use privileged intents.
3. Run:

```bash
python main.py
```

**Bot Commands**
- `!nasa_sat` — Sends today’s TrueColor satellite image.
- `!fires` — Sends today’s FIRMS thermal anomaly image.
- `!apod` — Sends today’s Astronomy Picture of the Day.
- `!helpme` — Shows the help text.

**Notes**
- The code saves a temporary file named `nasa_wallpaper.jpg` when fetching satellite images and removes it after sending.
- Adjust the `BBOX` and `WIDTH`/`HEIGHT` parameters in `nasa_func.py` if you need a different region or resolution.

**Files of interest**
- [main.py](main.py) — Discord bot commands and runner.
- [nasa_func.py](nasa_func.py) — Image fetching helpers.

## License
This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. 
Basically, you can do what you want as long as you keep it open source and give credit. 
See the [LICENSE](LICENSE) file for more details.

**Credits**
- NASA GIBS / FIRMS APIs for the amazing satellite data.
- Built by Feliks with 🐧 and Python.