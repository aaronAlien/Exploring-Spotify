# Spotify Data Analysis

Analysis of personal Spotify listening data using the Spotify Web API, with data processing and visualisation using Pandas, NumPy, Matplotlib, and Seaborn. Includes exploration of listening patterns alongside device usage data collected via Android developer tools.

### Analysis of my personal data using:
  - _Spotify web API | [spotify_listening.ipynb](https://github.com/aaronAlien/Exploring-Spotify/blob/main/spotify_listening.ipynb)_
  - _Android dev tools | [spotify_interaction.ipynb](https://github.com/aaronAlien/Exploring-Spotify/blob/main/spotify_interaction.ipynb)_
- _data visualisation with Pandas, Matplotlib, Seaborn, NumPy._


---

# Notes
- A big challenge here was expecting fom features to be available in the API which had recently been deprecated.
    - Spotify made [changes to the Web API](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api) which removed  most of the endpoints i was looking to explore.
    - I found no alternative method to replace the features for things such as tracks BPM and found comfirmation ont this - [reddit thread](https://www.reddit.com/r/spotifyapi/comments/1h1o2m9/spotify_api_changes/).

Even with the set back i believe the project went well. Having experience using API's in JavaScript i had to do some translating after not using utilising Python for some time.

- Intergrating other methods of data collection, as a lot of artists had no value for 'genres'. Even some of the most popular such as Tyler, The Creator. Therefore, i pulled artist data from Wikipedia as the html structure should be almost the same per artist page. Then, created the `getGenres()` function to target the data needed.

- Later created other functions such as `date_clean()` to also streamline the process.

- Explored different methods of data visualisation and a more artistic style with word clouds.


### _Android Debug Bridge_
Analysis of my daily interaction with the Spotify mobile app.

-   While it provides great insight into how often i use the mobile app, which is my main device. I also will use the app via other devices daily, therfore it's not the most accurate tracking of my spotify usage.
-   It was great to learn how to pull my personal usage stats with ADB and convert to csv for analysis. I created a [script with Tkinter](https://github.com/aaronAlien/Exploring-Spotify/blob/main/Convert_CSV/convert.py) (for a brain break with some frontend) that i could use daily.

## _Good stuff that helped:_

- [Spotify for Developers](https://developer.spotify.com/)
- [Android Debug Bridge (adb)](https://developer.android.com/tools/adb)
- [web scraping - elena tech](https://github.com/Elena-tech/web-scraping-lesson)
- [spotify api - elena tech](https://github.com/Elena-tech/api_lessons_101)
- [word cloud (at In:[35]) - areevesman](https://github.com/areevesman/spotify-wrapped/blob/main/code/01_Data_Visualization.ipynb)
- [my first attempt using a new api](https://github.com/aaronAlien/tfl_api)
- [sql visuals from when i first learnt SQL](https://dataschool.com/how-to-teach-people-sql/left-right-join-animated/)

---

### You will need to obtain an API key from [Spotify](https://developer.spotify.com/documentation/web-api)

`! pip install spotipy numpy pandas seaborn beautifulsoup4 matplotlib python-dotenv wordcloud pprint`

### spotify_listening.ipynb
Functions calling the API directly can have varied time range. time_range reference can be found [here](https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks)
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


