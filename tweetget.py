import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('EJKZi9KFhEFCMBpY7ubIbXI1A', '55gMFyF27AwIPxrzBNQd18vPq9ewdWFBqqMOKctv8NcUHqxEVx')
auth.set_access_token('744994747962499072-HlrStlnJt6ZvaiTnyI5yuwHNuUTecSw', 'LZpHpatb2bhE9rP4p6I0419ZWbvA3AK0T3YLsPl2WSZfQ')

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "#tigerking -filter:retweets",
                           since = "2020-03-24",
                           until = "2020-04-01",
                           lang = "en", count='100', tweet_mode='extended').items(10000):
    #u = api.get_user(tweet.id)
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.author._json['screen_name'], tweet.full_text.encode('utf-8')])
    print(tweet.created_at, tweet.author._json['screen_name'], tweet.full_text)
csvFile.close()
