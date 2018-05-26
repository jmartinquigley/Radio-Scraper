import requests as r
from bs4 import BeautifulSoup
import pandas as pd

#daily playlist off the ocean 1047 website. Need to create loop that goes through all dates using yyyy-mm-dd format
#dates = str(range(28))

playlists = "http://wocn.tunegenie.com/onair/2018-05-20/"

page = r.get(playlists)
soup = BeautifulSoup(page.text, 'html.parser')

songs = []
artists = []

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

#puts the information into a dataframe
df = pd.DataFrame(
        {'Song': songs,
         'Artist': artists})

#converts dataframe to csv file    
print(df)
#df.to_csv('test.csv')

""" TO DO:
        Create column for date.
        Create loop for multiple dates. Can likely do this through a list but that seems burdensome.
        """