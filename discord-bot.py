import os
import praw
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
DEBUG = conf.get('debug', None)
@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    while True:
        try:
            reddit = praw.Reddit(SITE)
            subreddit = reddit.subreddit(SUB)
            flairs = {str(fitem['user']):{'flair': fitem['flair_css_class'], 'text': fitem['flair_text']} for fitem in subreddit.flair(limit=None)}
            flairs.update({'N/A': 'N/A'})
            seen = []
            if DEBUG:
                print("Initialized.")
            for submission in subreddit.stream.submissions(skip_existing=True, pause_after=0):
                if submission is None:
                    await asyncio.sleep(.1)
                    continue
                if submission.approved and submission.id not in seen:
                    embed = discord.Embed(color=discord.Color.gold())
                    # embed.add_field(name=f"New Submission by {submission.author}", value=f"{submission.title}\n[Link to post](https://reddit.com{submission.permalink})")
                    embed.add_field(name="Title", value=item.title)
                    try:
                        embed.add_field(name="Content", value=item.self[:64])
                    except:
                        # embed.set_image(url=f"https://reddit.com{item.url}")
                        pass
                    seen.append(submission.id)
                    await channel.send(embed=embed)
        except Exception as e:
            with open('dbot-errors.txt', 'a') as f:
                f.write(f"{e}\n\n")
            continue
if __name__ == '__main__':
    bot.run(TOKEN)