# Import necessary libraries
import os
import time
import requests
import sys

# function to retrive Html-pages
def Retrive_html():
    for year in range(2013, 2019):
        for month in range(1, 13):
            if month < 10:
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month, year)
            else:
                 url = 'http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month, year)
            
            # getting and encoding the page
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')
            
            # Create the sub-directory Html_data if it does not exist
            if not os.path.exists("Data/Html_data/{}".format(year)):
                os.makedirs("Data/Html_data/{}".format(year))
            
            # open the directories and write the encoded data into them use wb to avoid byte code problems
            with open("Data/Html_data/{}/{}.html".format(year, month), "wb") as output:
                output.write(text_utf)
            
            sys.stdout.flush()

if __name__ == '__main__':
    start_time = time.time()
    Retrive_html()
    stop_time = time.time()
    print("Time Taken {}".format(stop_time - start_time))
