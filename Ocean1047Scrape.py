import requests as r
from bs4 import BeautifulSoup
import pandas as pd

#daily playlist off the ocean 1047 website. Need to create loop that goes through all dates using yyyy-mm-dd format

#the dd value works even if it's expressed as d

songs = []
artists = []

days = list(range(1,25))
#pulls and cleans all songs on the page.
print('Scraping website...')
for d in days:
    playlists = "http://wocn.tunegenie.com/onair/2018-05-"+str(d)+"/"
    page = r.get(playlists)
    soup = BeautifulSoup(page.text, 'html.parser')
    for i in soup.find_all('div', attrs={'class': 'large-9 small-8 columns hidden-on-open'}):
        left = i.find('div', attrs={'class': 'left'})
        song = left.find('div', attrs={'class': 'song'})
        songs.append(song.text)
#pulls and cleans ths artist list
    for i in soup.find_all('div', attrs={'class': 'large-9 small-8 columns hidden-on-open'}):
        left = i.find('div', attrs={'class': 'left'})
        artist = left.find('div', attrs={'class': None})
        artists.append(artist.text)
    global df
    df = pd.DataFrame(
        {'Song': songs,
         'Artist': artists})

#converts dataframe to csv file    
print('Exporting csv...')
df.to_csv('test.csv')

""" TO DO:
        Create column for date.
        """