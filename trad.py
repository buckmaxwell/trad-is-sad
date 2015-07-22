import requests
import pprint
import tweepy
import time
import random

def check_weather_if_raining_send_tweet():
	baseURL = 'http://api.openweathermap.org/data/2.5/weather?q=Columbus,oh'
	response = requests.get(baseURL)
	pp = pprint.PrettyPrinter(indent=4)
	dic = response.json()
	for w in dic['weather']:
		if 200 <= w['id'] < 600:
			tweet_sad_quote()
			print "HELLLLO!"
	pp.pprint(dic)

def tweet_sad_quote():
	CONSUMER_KEY = 'aRDgLpayyrEVOK1h18IbecTDZ'
	CONSUMER_SECRET = 'cITMUfgnAkPakRa6R3Pc3l4weHZJw5TlTkQhP1dqM657ikYBsi'
	ACCESS_TOKEN = '3385428580-TKJWheall40VEurl5vFe5txhdiK6glhhT5sOAwt'
	ACCESS_TOKEN_SECRET = 'uYz05eKZXZjlevxnTIDMPbp46b8XJI0HXoSAJzdNARzxB'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	status = get_sad_quote()
	if len(status) >140:
		while status:
			if len(status)>140:
				end=140 
			else:
				end=len(status)
			api.update_status(status=status[:end])
			status=status[140:]	
	api.update_status(status=status)



def get_sad_quote():
	result = None
	f=open('love.txt', 'r')
	random_number=random.randint(0,1568)
	for i, line in enumerate(f):
		if i==random_number:
			result = line
			break
	f.close()
	return result

def main():
	check_weather_if_raining_send_tweet()
	time.sleep(3600)




main()
