import requests as r
from bs4 import BeautifulSoup
import pandas as pd

timestamps = []
songs = []
artists = []

month = 4
days = list(range(1,2))

print('Scraping website...')

for d in days:
    playlists = "http://wocn.tunegenie.com/onair/2018-"+str(month)+"-"+str(d)+"/"
    page = r.get(playlists)
    soup = BeautifulSoup(page.text, 'html.parser')

#pulls and cleans the song played timestamp
    for i in soup.find_all('div', attrs={'class': 'large-3 small-4 columns text-right'}):
        timeclass = i.find('span', attrs={'class': 'timestamp'})
        stamp = (timeclass['data-date'])
        timestamps.append(stamp)
        
#pulls and cleans all songs on the page.    
    for i in soup.find_all('div', attrs={'class': 'large-9 small-8 columns hidden-on-open'}):
        left = i.find('div', attrs={'class': 'left'})
        song = left.find('div', attrs={'class': 'song'})
        songs.append(song.text)

#pulls and cleans ths artist list
    for i in soup.find_all('div', attrs={'class': 'large-9 small-8 columns hidden-on-open'}):
        left = i.find('div', attrs={'class': 'left'})
        artist = left.find('div', attrs={'class': None})
        artists.append(artist.text)
    
#puts the information into a single dataframe    
    global df
    df = pd.DataFrame(
        {'Timestamp' : timestamps,
         'Song': songs,
         'Artist': artists})

print(df.head)
#converts dataframe to csv file    
#print('Exporting csv...')
#df.to_csv(str(month)+'_songs.csv')

""" TO DO:
        Create column for date.
        """