import praw
from requests import Session
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):

    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    print("Sentence Overall Rated As", end = " ")

    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")

    else :
        print("Neutral")

session = Session()
session.verify = "/path/to/certfile.pem"

reddit = praw.Reddit(client_id='input id', client_secret='input secret', username='username', password='password', user_agent='reader by u/x')
print(reddit.user.me())


submission = reddit.submission(url=input("Input a reddit URL: "))
big_string = ''
count = 0
for comment in submission.comments:
    count += 1
    if count <=15:
        big_string += (str(comment.body) + '. ')

print(sentiment_scores(big_string))