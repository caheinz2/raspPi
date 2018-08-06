import tweepy
import json


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():

    #Import dev keys
    with open('credentials.json') as f:
        data = json.load(f)
        api = get_api(data)

    #Try out a tweet
    tweet = "Hello, world!"
    status = api.update_status(status=tweet)

    print "Done"

if __name__ == "__main__":
  main()
