import os
import praw
from configparser import ConfigParser
config = ConfigParser()
os.chdir(os.path.abspath(os.path.dirname(__file__)))
if os.path.exists('devconf.ini'):
    config.read('devconf.ini')
else:
    config.read('conf.ini')
conf = config['settings']

site = conf['test_praw_site']
sub = conf['test_subreddit']

def main(site, sub):
    reddit = praw.Reddit(site)
    reddit.validate_on_submit = True
    subreddit = reddit.subreddit(sub)
    for _ in range(5):
        subreddit.submit("here's something", "here's something else")
        print("Submitted a post. Awaiting approval.")

main(site, sub)