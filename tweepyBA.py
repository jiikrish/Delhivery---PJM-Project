from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
 
 
#consumer key, consumer secret, access token, access secret.
ckey="HVZVkdijtXdKPCB5BtOtLnnEY"
csecret="Zg8OsBUcsPwaWDmFqWU6BT1EMbNfGLTYkfgWJgLeq9itacYnG6"
atoken="787551178884120576-81OFAflVDzfeYNgtqmABte97RRUrfna"
asecret="CT27386gG61flGrgfwGdGxu6FcpMBEMtjiQrjOt6xBIm4"
 
class listener(StreamListener):
    #count=0
    def on_data(self, data):
 
        #while (count<10):
            #count = count+1
            tweet=data.split(',"text":"')[1].split('","source')[0]
            print(tweet+"\n")
            savefile=str(time.time())+"::"+tweet
            save=open('twitterdata1.csv','a')
            save.write(savefile)
            save.write("\n\n")
            save.close()
            return(True)

    def on_error(self, status):
        print (status)
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
 
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["chocolate day"]).items(50)

#HVZVkdijtXdKPCB5BtOtLnnEY API key

#Zg8OsBUcsPwaWDmFqWU6BT1EMbNfGLTYkfgWJgLeq9itacYnG6 secret key

#AAAAAAAAAAAAAAAAAAAAAER0HAEAAAAAJ7TWYRLuZIw2q%2Bqn1S3Ma5htrjw%3DQq38QMlsMZ2pN0jwte3hU1DW2zqNW7X77Pkx3SI7oJWTMk2C3W  token