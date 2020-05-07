# discord-notification-bot
It's pretty simple. Fill in these fields...

- `token`
- `praw_site`
- `subreddit`

...with the relevant info.

# Extra Config Options

There are extra options in the config, meant for use during debuggin of the bot script.

- `test_praw_site` - different account, to submit multiple submissons easily
- `test_subreddit` - a test subreddit to do them in (with approval ON)
- `debug` - print to the terminal "Initialized" when ready. otherwise, it's a silent script