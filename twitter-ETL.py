import tweepy
import pandas as pandas
import json
from datetime import datetime
import s3fs

# Access keys to ourL KPI
# access_key = "bw5XFG5j8oq3OIvpJQhTUKBiJ"
# access_secret = "8irHZWGDGLaZMqnhWEnZb8on2lWqDneImVwZ5RR5U1vtVse2OM"
# consumer_key = "1558032277359284224-adWUsuO0cuuFGdhvrVNfl2e3FLYkdN"
# consumer_secret = "NvBwJTI8aXQ6zbg4RERFt4t1vWXGJ4atLHa8nI0phu3Jh"


# # Twitter authentication
# auth = tweepy.OAuthHandler(access_key, access_secret)
# auth.set_access_token(consumer_key, consumer_secret)

# # Create an API object
# api = tweepy.API(auth)

# # Verify the credentials
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

# # Example of how to use the API: Getting your account's home timeline
# for tweet in api.home_timeline():
#     print(f"{tweet.user.name} said {tweet.text}")

# # Use the API to check your current rate limit status
# rate_limit_status = api.rate_limit_status()
# print(rate_limit_status)



# try:
#     # Your API call here
# except tweepy.RateLimitError:
#     print("Rate limit exceeded. Waiting before retrying...")
#     time.sleep(15 * 60)  # Wait for 15 minutes before retrying


# This code helps us manage rate limit


#import time

# # Your credentials
# API_KEY = 'your_api_key_here'
# API_KEY_SECRET = 'your_api_key_secret_here'


# ACCESS_TOKEN = 'your_access_token_here'
# ACCESS_TOKEN_SECRET = 'your_access_token_secret_here'

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create an API object
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# # Verify the credentials
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except Exception as e:
#     print("Error during authentication", e)

# # Fetching home timeline with rate limit handling
# def fetch_home_timeline():
#     try:
#         for tweet in tweepy.Cursor(api.home_timeline).items():
#             print(f"{tweet.user.name} said {tweet.text}")
#     except tweepy.RateLimitError:
#         print("Rate limit exceeded. Waiting before retrying...")
#         time.sleep(15 * 60)  # Wait for 15 minutes before retrying
#     except Exception as e:
#         print("An error occurred", e)

# fetch_home_timeline()



# Fetch the user timeline
# Fetch a user's timeline
# tweets = api.user_timeline(screen_name='@elonmusk',
#                            # 200 is the maximum allowed count
#                            count=200,
#                            include_rts=False,
#                            # Necessary to keep full_text
#                            # otherwise only the first 140 words are extracted
#                            tweet_mode='extended'
#                            )

# print(tweets)


# Search for recent tweets
# query = "from:elonmusk -is:retweet"  # Change the query to your preference
# try:
#     for tweet in tweepy.Cursor(api.search_tweets, q=query, tweet_mode='extended').items(200):
#         print(f"{tweet.user.name} said: {tweet.full_text}\n")
# except tweepy.RateLimitError:
#     print("Rate limit exceeded. Waiting before retrying...")
#     time.sleep(15 * 60)  # Wait for 15 minutes before retrying
# except Exception as e:
#     print("An error occurred", e)



# usernames = ["elonmusk"]
# try:
#     users = api.lookup_users(screen_names=usernames)
#     for user in users:
#         print(f"User: {user.screen_name}, Followers: {user.followers_count}, Location: {user.location}")
# except Exception as e:
#     print("An error occurred", e)


# tweet_ids = ["1278747501642657792", "1255542774432063488"]
# try:
#     tweets = api.statuses_lookup(tweet_ids, tweet_mode='extended')
#     for tweet in tweets:
#         print(f"{tweet.user.name} said: {tweet.full_text}\n")
# except Exception as e:
#     print("An error occurred", e)



# Twitter authentication
# auth = tweepy.OAuthHandler(access_key, access_secret)
# auth.set_access_token(consumer_key, consumer_secret)

# # Create an API object
# api = tweepy.API(auth)

# # Verify the credentials
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")


# Extract tweets
# def get_tweets(query, count):
#     tweets = tweepy.Cursor(api.search, q=query, lang="en").items(count)
#     tweet_list = [[tweet.created_at, tweet.text] for tweet in tweets]
#     return tweet_list

# tweets = get_tweets("#example", 100)

# access_key = "bw5XFG5j8oq3OIvpJQhTUKBiJ"
# access_secret = "8irHZWGDGLaZMqnhWEnZb8on2lWqDneImVwZ5RR5U1vtVse2OM"
# consumer_key = "1558032277359284224-adWUsuO0cuuFGdhvrVNfl2e3FLYkdN"
# consumer_secret = "NvBwJTI8aXQ6zbg4RERFt4t1vWXGJ4atLHa8nI0phu3Jh"



api_key = 'bw5XFG5j8oq3OIvpJQhTUKBiJ'
api_secret_key = '8irHZWGDGLaZMqnhWEnZb8on2lWqDneImVwZ5RR5U1vtVse2OM'
access_token = '1558032277359284224-adWUsuO0cuuFGdhvrVNfl2e3FLYkdN'
access_token_secret = 'NvBwJTI8aXQ6zbg4RERFt4t1vWXGJ4atLHa8nI0phu3Jh'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGXkuAEAAAAAc7loiciZ9J%2BRXhhAmWipgsLVBkQ%3DC6vhN4VParXHFhSGwp7hbxAuMYhDsDDPdrm6AWtxVQMZzVUfGB'

# # Authentification avec l'API v2
# client = tweepy.Client(bearer_token=bearer_token)

# # Fonction pour extraire les tweets
# def get_tweets_v2(query, max_results):
#     tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['created_at', 'text'])
#     tweet_list = []

#     for tweet in tweets.data:
#         tweet_list.append({"created_at": tweet.created_at, "text": tweet.text})
    
#     return tweet_list

# # Exemple d'utilisation
# query = "#example"
# tweets = get_tweets_v2(query, 100)  # 100 correspond au nombre de tweets que vous voulez récupérer
# print(json.dumps(tweets, indent=4))

# # Sauvegarder les tweets dans un fichier JSON
# with open("tweets_v2.json", "w") as file:
#     json.dump(tweets, file)


# Authentification avec l'API v1.1 et l'API v2



client = tweepy.Client(bearer_token=bearer_token)
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Fonction pour rechercher des tweets récents
def search_tweets(query, max_results):
    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['created_at', 'text'])
    tweet_list = []

    for tweet in tweets.data:
        tweet_list.append({"created_at": tweet.created_at, "text": tweet.text})
    
    return tweet_list

# Fonction pour récupérer des informations sur un utilisateur
def get_user_info(username):
    user = client.get_user(username=username, user_fields=['created_at', 'description', 'public_metrics'])
    user_info = {
        "username": user.data.username,
        "name": user.data.name,
        "created_at": user.data.created_at,
        "description": user.data.description,
        "followers_count": user.data.public_metrics['followers_count'],
        "following_count": user.data.public_metrics['following_count'],
        "tweet_count": user.data.public_metrics['tweet_count']
    }
    return user_info

# Fonction pour poster un nouveau tweet
def post_tweet(status):
    response = api.update_status(status=status)
    return response._json

# Exemple d'utilisation

# Rechercher des tweets récents
query = "#example"
tweets = search_tweets(query, 10)
print("Tweets:")
print(json.dumps(tweets, indent=4))

# Récupérer des informations sur un utilisateur
username = "twitter"
user_info = get_user_info(username)
print("\nUser Info:")
print(json.dumps(user_info, indent=4))

# Poster un nouveau tweet
status = "Hello, this is a tweet from Tweepy!"
tweet_response = post_tweet(status)
print("\nPosted Tweet:")
print(json.dumps(tweet_response, indent=4))

# Sauvegarder les tweets dans un fichier JSON
with open("tweets.json", "w") as file:
    json.dump(tweets, file)

# Sauvegarder les informations utilisateur dans un fichier JSON
with open("user_info.json", "w") as file:
    json.dump(user_info, file)

# Sauvegarder le tweet posté dans un fichier JSON
with open("tweet_response.json", "w") as file:
    json.dump(tweet_response, file)