# RhythmRanger

## Description
My Music Bot is a Discord bot that allows users to play music in voice channels. It supports playing music from YouTube by URL or by searching for keywords.

## Features
- Play music from YouTube by URL or by search keywords
- Queue system to add multiple songs for playback
- Skip, pause, resume, and stop playback commands
- Display current playing song information
- Display the queue of upcoming songs
- Help command to provide information about available commands

## Installation
1. Clone the repository: `git clone https://github.com/LiquorProg/RhythmRanger.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a `config.py` file with your Discord bot token.
4. You will also need to download the FFmpeg player and place it in a folder with main.py
5. Run the bot: `python main.py`

## Usage
1. Invite the bot to your Discord server by visiting the following URL: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=1103331095891693651&permissions=274914609152&scope=bot)
2. Join a voice channel in your server
3. Use the following commands:
   - `!join`: Join the voice channel
   - `!leave`: Leave the voice channel
   - `!play <url or search keywords>`: Play a song by URL or search keywords
   - `!skip`: Skip the currently playing song
   - `!pause`: Pause the currently playing song
   - `!resume`: Resume playback of the paused song
   - `!stop`: Stop playback and clear the queue
   - `!queue`: Display the queue of upcoming songs
   - `!help`: Show the list of available commands

## License
Project katalog is distributed under the MIT license.
