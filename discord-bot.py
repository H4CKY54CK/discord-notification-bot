import os
import sys
import praw
import time
import asyncio
import discord
from configparser import ConfigParser
config = ConfigParser()
os.chdir(os.path.abspath(os.path.dirname(__file__)))
if os.path.exists('devconf.ini'):
    config.read('devconf.ini')
else:
    config.read('conf.ini')
conf = config['settings']
TOKEN = conf['token']
SITE = conf['praw_site']
SUB = conf['subreddit']
CHANNEL_ID = conf.getint('channel_id')
bot = discord.Client()
@bot.event
async def on_ready():
    ctx = bot.get_channel(CHANNEL_ID)
    while True:
        try:
            reddit = praw.Reddit(SITE)
            subreddit = reddit.subreddit(SUB)
            for submission in subreddit.stream.submissions(skip_existing=True, pause_after=0):
                if submission is None:
                    await asyncio.sleep(.1)
                    continue
                embed = discord.Embed(color=discord.Color.gold())
                embed.add_field(name=f"New Submission by {submission.author}", value=f"{submission.title}\n[Link to post](https://reddit.com{submission.permalink})")
                await ctx.send(embed=embed)
        except Exception as e:
            continue

if __name__ == '__main__':
    sys.exit(bot.run(TOKEN))