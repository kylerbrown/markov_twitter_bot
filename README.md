# markov twitter bot

A simple twitterbot for posting markov chain generated tweets.

## requirements

+ Python 3 (2 might work)
+ PyMarkovChain `git clone https://github.com/TehMillhouse/PyMarkovChain.git && cd PyMarkovChain && pip install -e .`
+ Twython `pip install twython`

## usage

+ Get a [Twitter API Key](https://dev.twitter.com/apps), by registering an app and obtaining consumer and access keys.
+ create `twitter_api_key.py` and place the following contents in it:
```
key = {"consumer_key": "XXXXXXXXXX",
	"consumer_secret": "XXXXXXXXXX",
	"access_token_key": "XXXXXXXXX",
	"access_token_secret": "XXXXXX"}
```
replacing the `XXXX`s with the appropriate strings.
+ `git clone https://github.com/kylerbrown/markov_twitter_bot.git`
+ create a file with text to fill the Markov chain database, called `data.txt`.
+ run `python markov.py data.txt` to manually filter markov generated text, this will create a file with a queue of tweets.
+ setup cron, with crontab -e and run `/path/to/python /path/to/tweeter.py `. for example,

```
# m h  dom mon dow   command
  0 2  *   *   *     /usr/bin/python ~/markov_twitter/tweeter.py ~/markov_twitter/tweets.txt
```
  will generate a tweet once a day at 2:00 a.m..
