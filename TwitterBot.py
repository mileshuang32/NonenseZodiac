import tweepy
import time
import markovify
import random
import os
from datetime import date
horoscopes =['ARIES ♈:','TAURUS ♉:','GEMINI ♊:','CANCER ♋:','LEO ♌:','VIRGO ♍:','LIBRA ♎:','SCORPIO ♏:','SAGITTARIUS ♐:','CAPRICORN ♑:','AQUARIUS ♒:','PISCES ♓:']
with open("Horo.txt") as f:
    text = f.read()

CONSUMER_KEY = 'INSERT YOUR COMSUMER KEY HERE'
CONSUMER_SECRET = 'INSERT YOUR SECRET HERE'
ACCESS_KEY = 'INSERT YOUR ACCESS KEY HERE'
ACCESS_SECRET = 'INSERT YOUR ACCESS KEY HERE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) 
api = tweepy.API(auth)
today = date.today()
today_formatted = today.strftime("%B %d, %Y")
for i in range(12):
    text_model = markovify.Text(text)
    random_choice=random.choice(horoscopes)
    textOfTheDay=text_model.make_short_sentence(150)
    textOfTheDay=random_choice+textOfTheDay+' ——'+today_formatted
    if(random_choice=='ARIES ♈:'):
        image = "Aries.jpg"
    elif (random_choice=='TAURUS ♉:'):
        image = "Taurus.jpg"
    elif (random_choice=='GEMINI ♊:'):
        image = "Gemini.jpg"
    elif (random_choice=='LEO ♌:'):
        image = "Leo.jpg"
    elif (random_choice=='VIRGO ♍:'):
        image = "Virgo.jpg"
    elif (random_choice=='LIBRA ♎:'):
        image = "Libra.jpg"
    elif (random_choice=='SCORPIO ♏:'):
        image = "Scorpio.jpg"
    elif (random_choice=='SAGITTARIUS ♐:'):
       image = "Sagittarius.jpg"
    elif (random_choice=='CAPRICORN ♑:'):
        image = "Capricorn.jpg"
    elif (random_choice=='AQUARIUS ♒:'):
        image = "Aquarius.jpg"
    elif (random_choice=='PISCES ♓:'):
        image = "Pisces.jpg"
    elif (random_choice=='CANCER ♋:'):
        image = "Cancer.jpg"
    horoscopes.remove(random_choice)
    api.update_with_media(image,textOfTheDay)
    print(textOfTheDay)
    time.sleep(15)



