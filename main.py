from google_currency import convert  
import json
import os

from dotenv import load_dotenv
import tweepy as tp
import sys 


load_dotenv()
print ("START")

# credentials to login to twitter api

try:
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_secret = os.getenv('ACCESS_SECRET')
except:
    sys.exit("Você esqueceu de carregar as credenciais")
   

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

try:
    os.system("echo START")
    os.system("rm yocurrency/output.json")
    os.system("cd yocurrency && scrapy crawl tata -o output.json --nolog")
except:
    os.system("deu pau")
    pass

usd2brl = convert('usd', 'brl', 1)
usd2brl_short = float(usd2brl[40:-21:])


with open('yocurrency/output.json') as f:
    data = json.load(f)
f.close

# conversion json -> float
tata_brl = float(data[0].get("price")[2::].replace(',','.'))

tata2usd = usd2brl_short/tata_brl
tweet = "Um dólar é equivalente a %.2f tatás de flocos." % tata2usd
api.update_status(tweet)


