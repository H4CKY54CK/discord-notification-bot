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
        for submission in subreddit.stream.submissions(skip_existing=True, pause_after=0):
            if submission is None:
                continue
            embed = discord.Embed(color=discord.Color.gold())
            embed.add_field(name=f"New Submission by {submission.author}", value=f"{submission.title}\n[Link to post](https://reddit.com{submission.permalink})")
            await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
if __name__ == '__main__':
    reddit = praw.Reddit(SITE)
    subreddit = reddit.subreddit(SUB)
    bot.run(TOKEN)