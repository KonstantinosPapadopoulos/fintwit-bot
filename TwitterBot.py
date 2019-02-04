import tweepy
import requests
import json
import time
import Credentials as c






sources = ['bloomberg','financial-times','cnbc','reuters','al-jazeera-english','the-wall-street-journal','the-huffington-post','business-insider','the-new-york-times']

auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)

auth.set_access_token(c.access_token, c.access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object


def getTimelineTweets():
    tweets = api.home_timeline()
    for tweet in tweets:
        print(tweet.text)

def getFollowers(username):
    user = api.get_user(username)
    for follower in user.followers():
        print(follower.screen_name)

def getFollowing(username):
    user = api.get_user(username)
    for following in user.friends():
        print(following.screen_name)

def tweet(message):
    api.update_status(message)


def getNews(newsSource):
    resp = requests.get('https://newsapi.org/v1/articles?source='+ newsSource + '&apiKey=' + c.newsAPI)
    j = resp.json()
    return j

def getTopArticle(json):
    return json['articles'][0]


if __name__ == '__main__':

    while True:

        for source in sources:
            article = getTopArticle(getNews(source))

            message = article['title'] + " " + article['url']

            try:
                tweet(message)
            except:
                print("Error")
                continue

            time.sleep(7200)

