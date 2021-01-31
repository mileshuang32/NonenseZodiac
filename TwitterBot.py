import tweepy
import time
import markovify
import random
import os
from datetime import date
# Created a list of the 12 zodiac sighs with emojis.
horoscopes =['ARIES ♈:','TAURUS ♉:','GEMINI ♊:','CANCER ♋:','LEO ♌:','VIRGO ♍:','LIBRA ♎:','SCORPIO ♏:','SAGITTARIUS ♐:','CAPRICORN ♑:','AQUARIUS ♒:','PISCES ♓:']
# Open the traning data file 
with open("HoroscopeTraining.txt") as f:
    text = f.read()

# Tweepy functions for accessing the twitter account and authorize usage
CONSUMER_KEY = 'INSERT YOUR COMSUMER KEY HERE'
CONSUMER_SECRET = 'INSERT YOUR SECRET HERE'
ACCESS_KEY = 'INSERT YOUR ACCESS KEY HERE'
ACCESS_SECRET = 'INSERT YOUR ACCESS KEY HERE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) 
api = tweepy.API(auth)
# Get today's date
today = date.today()
# Change data format to Month-Day-Year
today_formatted = today.strftime("%B %d, %Y")
# Loop through the List and select all the zodiac signs
for i in range(12):
    # Train the markov engine based on the training data and return a model
    text_model = markovify.Text(text)
    # Randomly select a horoscope from the list
    random_horoscopes=random.choice(horoscopes)
    # Construct the daily prediction based on the traning model with less or equal to 150 characters
    textOfTheDay=text_model.make_short_sentence(150)
    # Construct the tweet with the selected horoscope, the daily prediction and the current date
    textOfTheDay=random_horoscopes+textOfTheDay+' ——'+today_formatted
    # Depending on the horoscope, upload a preselected image of the horoscope
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
    # Remove the selected horoscope so that each horoscope is only tweeted once
    horoscopes.remove(random_horoscopes)
    # Upload the text along with the corresponding image
    api.update_with_media(image,textOfTheDay)
    print(textOfTheDay)
    # Wait 15 second before posting the next tweet
    time.sleep(15)



