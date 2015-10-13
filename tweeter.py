from twython import Twython
from twitter_api_key import key
from argparse import ArgumentParser


def setup_api(key):
    t = Twython(app_key=key["consumer_key"],
                app_secret=key["consumer_secret"],
                oauth_token=key["access_token_key"],
                oauth_token_secret=key["access_token_secret"])
    return t


def check_times(lst):
    for l in lst:
        print("tweet time: ", int(l))


def get_tweet(tweetfile):
    with open(tweetfile, 'r') as f:
        first_line = f.readline().strip()
    return first_line


def remove_tweet(tweetfile):
    with open(tweetfile, 'r') as f:
        lines = f.readlines()
    with open(tweetfile, 'w') as f:
        [f.write(line) for line in lines[1:]]
    return True


def tweeter(tweetfile, times, cronmode=False):
    if not cronmode:
        check_times(times)
        # wait for tweet time
        raise NotImplementedError

    # get text line
    tweet_text = get_tweet(tweetfile)
    if not tweet_text:
        raise Exception("tweet file empty")
    # tweet text
    api = setup_api(key)
    status = api.update_status(status=tweet_text)
    # if success, delete line
    if status:
        remove_tweet(tweetfile)


def main():
    parser = ArgumentParser()
    parser.add_argument("tweetfile",
                        help="name of file with generated tweets",
                        default=None)
    parser.add_argument("-i", "--interval",
                        help="a list of hours to tweet, not yet implemented",
                        default=[0],
                        nargs='+')
    parser.add_argument("--cronmode",
                        help="runs script in chronmode (tweets and exits)",
                        default=False, action="store_true")

    args = parser.parse_args()
    tweeter(args.tweetfile, args.interval, args.cronmode)

if __name__ == "__main__":
    main()
