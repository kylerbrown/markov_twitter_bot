from pymarkovchain import MarkovChain
from argparse import ArgumentParser

sentence_regex = """(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"""

default_markovbdname = "./markovdb"

def build_database(dbasefname, textfile, sregex):
    if not (dbasefname or textfile):
        raise Exception("must input either an existing \
        database or data textfile")
    if textfile:
        mc = MarkovChain(default_markovbdname)
        with open("data.txt", "r") as f:
            mc.generateDatabase(f.read(),
                                sentenceSep=sregex,
                                n=2)
    elif dbasefname:
        mc = MarkovChain(dbasefname)
    return mc


def gen_tweet(mc):
    while True:
        tweet = mc.generateString()
        if len(tweet) < 129 and len(tweet) > 40:
            return tweet + " #analytics"


def tweet_to_file(tweet, tfile):
    with open(tfile, "a") as f:
        f.write(tweet + "\n")


def manual_review(tweet_file, mc):
    response = ""
    while not response == "q":
        possible_tweet = gen_tweet(mc)
        print(possible_tweet)
        response = input("q: exit\ny: accept\nn: reject\n")
        if response == "y":
            tweet_to_file(possible_tweet, tweet_file)


def markov(textfile, outfile, database, sregex):
    mc = build_database(database, textfile, sregex)
    manual_review(outfile, mc)
    saved = mc.dumpdb()
    if saved:
        print("database saved to ", mc.dbFilePath)


description = """markov.py -- an interface to generate random sentences based on
input text"""


def main():
    parser = ArgumentParser(description=description)
    parser.add_argument("textfile", help="source data file",
                        default=None, nargs="?")
    parser.add_argument("-d", "--database", help="name of database file",
                        default=None)
    parser.add_argument("-o", "--out", help="name of output file",
                        default="tweets.txt", nargs=1, type=str)
    parser.add_argument("--regex", help="sentence separator regex",
                        default=sentence_regex, nargs=1, type=str)

    args = parser.parse_args()
    markov(args.textfile, args.out, args.database, args.regex)


if __name__ == "__main__":
    main()
