import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_keys import get_credentials
import pandas as pd
import time

cid, secret = get_credentials()

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

#ids = getTrackIDs('Susanna Ketola', '4rnleEAOdmFAbRcNCgZMpY')
ids = getTrackIDs('levonh', '0Opo3iNacA5BzCSn8ldxmX')

def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)
    # meta
    name = meta['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    #explicit = features[0]['explicit']
    key = features[0]['key']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    mode = features[0]['mode']
    duration_ms = features[0]["duration_ms"]
    time_signature = features[0]['time_signature']

    track = [name, id, artist, release_date, duration_ms, length, key, popularity, mode, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

# loop over track ids 
tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

# create dataset
df = pd.DataFrame(tracks, columns = ["name", "id", "artist", "release_date", "duration_ms", "length", "key", "popularity", "mode", "danceability", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "tempo", "time_signature"])
df.to_csv("data_sample.csv", sep = ',')

