import requests
from bs4 import BeautifulSoup

'''
import tweepy

CONSUMER_KEY = 'aRDgLpayyrEVOK1h18IbecTDZ'
CONSUMER_SECRET = 'cITMUfgnAkPakRa6R3Pc3l4weHZJw5TlTkQhP1dqM657ikYBsi'
ACCESS_TOKEN = 3'385428580-TKJWheall40VEurl5vFe5txhdiK6glhhT5sOAwt'
ACCESS_TOKEN_SECRET = 'uYz05eKZXZjlevxnTIDMPbp46b8XJI0HXoSAJzdNARzxB'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
'''


sc = 200
baseURL = 'http://www.goodreads.com/quotes/tag/sadness?page='
pn = 1

f = open('love.txt', 'w')
f.write('\n')
f.close()


while sc == 200:
	response =requests.get(baseURL + str(pn))
	soup = BeautifulSoup(response.text)
	ql = soup.find_all(class_="quoteText")

	for q in ql:
		quote = q.text.split('//<![CDATA[')[0].encode('utf-8').replace('\t', '').replace('\n', '').split('function submit')[0]
		print quote + '\n'
		f = open('love.txt', 'a')
		f.write(quote + '\n')
		f.close()

	pn += 1
	sc = response.status_code
