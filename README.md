# gpu-bot

Reddit bot for tracking GPU deals

Built with [PRAW](https://praw.readthedocs.io/en/latest/index.html) Reddit API wrraper

## How the bot works
The deal alert is sent via email.  
The bot is searching for new listings of GPU sales in the [buildapcsales](https://www.reddit.com/r/buildapcsales/) subreddit.  
Every 15 minutes a query is made, and if a new deal is detected, an email is sent to the provided destination.

## How to use
There are 5 environment variables that need to be set - either in a .env file or the shell.
* CLIENT_ID - reddit bot client id
* CLIENT_SECRET - reddit bot client secret
* USER_EMAIL - the email address that will be the sender. **Attention:** Hard codded to be an **outlook** mail.
* USER_PASS - password for the above email adderss.
* DESTINATION - an email adderss to recieve the message - can be from any provider.

## Deployment
The bot can be deployed on a remote cloud environment.  
The Procfile is for the [Heroku](https://www.heroku.com/) platfrom.
