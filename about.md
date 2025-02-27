# Spotify Data Analysis

## _General_
- ``.concat()`` used frequently (in both notebooks) to gather df's with identical columns. then ``.reset_index(drop=(True)`` to create one new index for the new concat df

- finding a color scheme 'plasma' greatly increased my satisfaction with the data visuals. pulling the colormap and applying to the plot:

```
colors = plt.cm.plasma(np.linspace(0, 1, len(all_top_artists)))
sns.barplot(x=list(genre_count.values()), y=list(genre_count.keys()), palette=colors)
```

## _Spotify Web API_
- analysis of my personal spotify data
- data visualisation with Pandas, Matplotlib, Seaborn, NumPy.
#
- A big challenge here was expecting fom features to be available in the API which had recently been depecated.
    - Spotify made [changes to the Web API](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api) which removed  most of the endpoints i was looking to explore.
    - I found no alternative method to replace the features for things such as tracks BPM and found i am far from the only person dissapointed by these changes - [reddit thread](https://www.reddit.com/r/spotifyapi/comments/1h1o2m9/spotify_api_changes/).

- Even with the set back i belive the project went well:
    - I've made so much progess with Python after not applying the language for a while. Having experience using API's in JS i knew how to get to point that i wanted but would have to push myself using Python.
    - Intergrating other methods of getting data, web scraping.
    
        - I was surprised that a lot of artists had no value for 'genres' even some of the most popular such as Tyler, The Creator.
        - Went to wikipedia as the html structure should be almost the same per artist.
        - I did have a small struggle as the 'Genres' would not always be in the same index per table. This was one of many learning curves, improving my Python skills in the `getGenres()` function.
    - I refractored a few times. Where i wanted to make sure i was getting the right data first i split the code in small sections. Later created functions to make the process easier such as `date_clean()`.
    - Finding different ways to display data was a challenge as my project direct changed from the initial plan. However i explored ways to edit plots


### _Android Debug Bridge_
- analysis of my daily interaction with the Spotify mobile app.
    - This was the back up plan as i did not recieve my personal data (upon request) from Spotify in time.
    -   While it provides great insight into how often i use the mobile app, which is my main device. I also will use the iPad app daily, therfore it's not the most accurate tracking of my spotify usage.
    -   It was great to learn how to pull my personal usage stats with ADB and convert to csv for analysis.
        - because i was prearing to do this a few times i created a little app that i could use daily. 

# _good stuff that helped:_

- [Spotify for Developers](https://developer.spotify.com/)
- [Android Debug Bridge (adb)](https://developer.android.com/tools/adb)
#
- [web scraping - elena tech](https://github.com/Elena-tech/web-scraping-lesson)
- [spotify api - elena tech](https://github.com/Elena-tech/api_lessons_101)
- [word cloud (at In:[35]) - areevesman](https://github.com/areevesman/spotify-wrapped/blob/main/code/01_Data_Visualization.ipynb)
#
- [my first attempt using a new api](https://github.com/aaronAlien/tfl_api)
- [sql visuals from when i first learnt SQL](https://dataschool.com/how-to-teach-people-sql/left-right-join-animated/)
#

