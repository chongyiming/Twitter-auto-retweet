import tweepy
import time
apikey="kaRx19Q0bqjG4tTgBmD6JOx5B"
apikeysecret="eVJRKP3QW1t3UhEext9sU8GfgmKi0GrzwsGRFGP8jdMUoIhMXj"
bearer='AAAAAAAAAAAAAAAAAAAAACvbwgEAAAAAIGj81GZya1s1snqMXN3w9vRD3R0%3DfmNBSacsk3KkJlR173eeraRfQA5bJWY6IumHbfSB8WtTmIb2tE'
accesstoken='1586035484073295873-QIctCy1Z5RaKuQkCXMS8u6S1lhHqSF'
accesstokensecret='s02JThwDkHHERJIqhcWut6jEO5OlzO16QvjFyizAf0CQH'

client=tweepy.Client(bearer,apikey,apikeysecret,accesstoken,accesstokensecret)
auth=tweepy.OAuth1UserHandler(apikey,apikeysecret,accesstoken,accesstokensecret)
api=tweepy.API(auth)
tweet_id = '1852286733205074091'

time.sleep(3600)
while True:
    try:
        client.retweet(tweet_id)
        print(f"Retweeted: {tweet_id}")
        break
    except:
        time.sleep(60)
