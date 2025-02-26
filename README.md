# Explore My World of Music

### Tech used:
[Spotify API]('https://developer.spotify.com/)

[Android Debug Bridge (adb)]('https://developer.android.com/tools/adb)

`! pip install spotipy numpy pandas seaborn beautifulsoup4 matplotlib python-dotenv wordcloud pprint`


#### Spotify_listening.ipynb
- my spotify data from the Spotify Web API.
- functions calling the API directly can have varied time range:
    - time_range reference can be found [here](https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks)
```
def get_artists(time_range='long_term', limit=20):
    results = sp.current_user_top_artists(time_range=time_range, limit=limit)
    artists = []

    for item in results['items']:
        genres = item.get('genres')
        artists.append({
            'name': item['name'],
            'genres': ', '.join(item['genres']),
            'popularity': item['popularity'],
            'followers': item['followers']['total'],
        })
    df = pd.DataFrame(artists)

    # add other for empty genre lists
    # later - adding genres from get_genres() function.
    df['Genres'] = df['genres'].apply(lambda x: x if x else 'other')

    return df
```
- then pass time range or default = 'medium_term'
```
my_artists_df = get_artists('short_term')
```



####  spotify_interactions.ipynb
    - collecting my mobile Spotify usage data from android, daily.
    
    - ouput shows interactions with the app per day from a selection of activity types.

## see _about.md_ for project report