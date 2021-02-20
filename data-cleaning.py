import json
import pandas as pd
import numpy as np

# Read in the 3 JSONs
with open('generated_songs.json') as f:
    track_data = json.load(f)
with open('generated_artists.json') as f:
    artist_data = json.load(f)
with open('artist_genres.json') as f:
    aGenre_data = json.load(f)

# Bin the artists into genres...
# 1) Grab all possible genres from the recommended artists
genre_dist = dict()
for genres_lst in aGenre_data.values():
    for genre in genres_lst:
        if genre not in genre_dist.keys():
            genre_dist[genre] = 1
        else:
            genre_dist[genre] += 1

# Output to dataframe
genre_dist = pd.DataFrame(genre_dist.items(), columns=['Genre','Freq'])
genre_dist.set_index('Genre',inplace=True)

# Bin the data
genre_bins = {
    'Indie': [],
    'Dance': [],
    'Rap': [],
    'Pop': [],
    'Country': [],
    'Misc.': []
}
indie_rules = ['indie']
dance_rules = ['dance','house', 'edm', 'techno']
rap_rules = ['rap', 'trap']
pop_rules = ['pop']
country_rules = ['country']
for genre in list(genre_dist.index):
    assigned = False
    # Create and enforce rules for binning indie music
    for rule in indie_rules:
        if rule in genre.split():
            genre_bins['Indie'].append(genre)
            assigned = True
    if not assigned:
        for rule in dance_rules:
            if rule in genre.split():
                genre_bins['Dance'].append(genre)
                assigned = True
    if not assigned:
        for rule in rap_rules:
            if rule in genre.split():
                genre_bins['Rap'].append(genre)
                assigned = True
    if not assigned:
        for rule in pop_rules:
            if rule in genre.split():
                genre_bins['Pop'].append(genre)
                assigned = True
    if not assigned:
        for rule in country_rules:
            if rule in genre.split():
                genre_bins['Country'].append(genre)
                assigned = True
    if not assigned:
        genre_bins['Misc.'].append(genre)

# The genres are now binned. Now, calculate some statistics for each genre.
indie_artist = []
for artist in artist_data:
    assigned = False
    for genre in artist['genres']:
        if not assigned:
            if genre in genre_bins['Indie']:
                indie_artist.append(artist)
                assigned = True
followers = np.asarray([])
popularities = np.asarray([])
for artist in indie_artist:
    followers = np.append(followers, artist['followers']['total'])
    popularities = np.append(popularities, artist['popularity'])
indie_stats = {
    "min_followers": min(followers),
    "mean_followers": np.mean(followers),
    "max_followers": max(followers),
    "min_popularity": min(popularities),
    "mean_popularity": np.mean(popularities),
    "max_popularity": max(popularities)
}
# Dance artists
dance_artist = []
for artist in artist_data:
    assigned = False
    for genre in artist['genres']:
        if not assigned:
            if genre in genre_bins['Dance']:
                dance_artist.append(artist)
                assigned = True
followers = np.asarray([])
popularities = np.asarray([])
for artist in dance_artist:
    followers = np.append(followers, artist['followers']['total'])
    popularities = np.append(popularities, artist['popularity'])
dance_stats = {
    "min_followers": min(followers),
    "mean_followers": np.mean(followers),
    "max_followers": max(followers),
    "min_popularity": min(popularities),
    "mean_popularity": np.mean(popularities),
    "max_popularity": max(popularities)
}
# Rap
rap_artist = []
for artist in artist_data:
    assigned = False
    for genre in artist['genres']:
        if not assigned:
            if genre in genre_bins['Rap']:
                rap_artist.append(artist)
                assigned = True
followers = np.asarray([])
popularities = np.asarray([])
for artist in rap_artist:
    followers = np.append(followers, artist['followers']['total'])
    popularities = np.append(popularities, artist['popularity'])
rap_stats = {
    "min_followers": min(followers),
    "mean_followers": np.mean(followers),
    "max_followers": max(followers),
    "min_popularity": min(popularities),
    "mean_popularity": np.mean(popularities),
    "max_popularity": max(popularities)
}
# Pop
pop_artist = []
for artist in artist_data:
    assigned = False
    for genre in artist['genres']:
        if not assigned:
            if genre in genre_bins['Pop']:
                pop_artist.append(artist)
                assigned = True
followers = np.asarray([])
popularities = np.asarray([])
for artist in pop_artist:
    followers = np.append(followers, artist['followers']['total'])
    popularities = np.append(popularities, artist['popularity'])
pop_stats = {
    "min_followers": min(followers),
    "mean_followers": np.mean(followers),
    "max_followers": max(followers),
    "min_popularity": min(popularities),
    "mean_popularity": np.mean(popularities),
    "max_popularity": max(popularities)
}
# Country
country_artist = []
for artist in artist_data:
    assigned = False
    for genre in artist['genres']:
        if not assigned:
            if genre in genre_bins['Country']:
                country_artist.append(artist)
                assigned = True
followers = np.asarray([])
popularities = np.asarray([])
for artist in country_artist:
    followers = np.append(followers, artist['followers']['total'])
    popularities = np.append(popularities, artist['popularity'])
country_stats = {
    "min_followers": min(followers),
    "mean_followers": np.mean(followers),
    "max_followers": max(followers),
    "min_popularity": min(popularities),
    "mean_popularity": np.mean(popularities),
    "max_popularity": max(popularities)
}
# Misc.
misc_artist = []
for artist in artist_data:
    assigned = False
    for genre in artist['genres']:
        if not assigned:
            if genre in genre_bins['Misc.']:
                misc_artist.append(artist)
                assigned = True
followers = np.asarray([])
popularities = np.asarray([])
for artist in misc_artist:
    followers = np.append(followers, artist['followers']['total'])
    popularities = np.append(popularities, artist['popularity'])
misc_stats = {
    "min_followers": min(followers),
    "mean_followers": np.mean(followers),
    "max_followers": max(followers),
    "min_popularity": min(popularities),
    "mean_popularity": np.mean(popularities),
    "max_popularity": max(popularities)
}

# Now, output to csv files
df = pd.DataFrame.from_dict(indie_stats, orient='index',columns=['indie'])
df['dance'] = pd.DataFrame.from_dict(dance_stats, orient='index')
df['rap'] = pd.DataFrame.from_dict(rap_stats, orient='index')
df['pop'] = pd.DataFrame.from_dict(pop_stats, orient='index')
df['country'] = pd.DataFrame.from_dict(country_stats, orient='index')
df['misc'] = pd.DataFrame.from_dict(misc_stats, orient='index')
df_t = df.transpose()

# Followers data
df_t['min_followers'].to_csv('csv_data/min_follower_data.csv', header=False)
df_t['mean_followers'].to_csv('csv_data/mean_follower_data.csv', header=False)
df_t['max_followers'].to_csv('csv_data/max_follower_data.csv', header=False)
