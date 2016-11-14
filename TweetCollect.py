from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key='oXdbNFctfSb7sRINv0aWJdXs0'
consumer_secret='ejYi3aYglTe4lKdL88hPv6VLkEQPS83O4ffku0sCPjOJ44mMYj'
access_token='1633855369-g9F2wjzH2k2V0kIDkCw13fKinQ1l7u3ex0zw6NJ'
access_token_secret='E5FiQAWDHiR4nSDvJnB4TGRUAOTDElfsUNkRov5laCobT'

text_file = open("/media/atanu/New Volume/Tweet-analysis/streamingData.json", "a")

class listener(StreamListener):
    def on_data(self, data):
        twt =data

        text_file.write(twt+'\n')
        print twt
        return True
    def on_error(self, status):
         print status
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["election"])
