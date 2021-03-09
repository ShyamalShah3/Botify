import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
def randomMusic():
  sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials ("5f75bd64fe6742598b2d4650d401e9fe", "bf777b8578dd4f55b25b31f768eec9c2"))
  genres = sp.recommendation_genre_seeds()
  # print("Here are all genres avaliable:")
  # print(genres['genres'])
  # print()
  # inputGenre = input("Which genre do you like?: ")
  inputGenre = genres['genres'][random.randint(0, len(genres['genres'])-1)]
  search = sp.search(q = inputGenre, limit = 1)
  ge = [inputGenre]
  track_id = [search['tracks']['items'][0]['id']]
  recommendations = sp.recommendations(seed_genres = ge, limit = 10)
  tracks = recommendations['tracks']
  link = tracks[0]["album"]['id']
  return link
  # i = 1
  # for track in tracks:
  #   print(str(i) +". Name: "+ track['name'] + "\tArtist: " + track['artists'][0]['name'])
  #   print("Link: " + track['external_urls']['spotify']+ "\n");
  
  #   i+=1
def personalRecom(genres, artists, tracks):
  sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials ("5f75bd64fe6742598b2d4650d401e9fe", "bf777b8578dd4f55b25b31f768eec9c2"))
  
  inputG = [genres]
  searchA = sp.search(q = artists, limit = 1)
  inputa = searchA["tracks"]["items"][0]["artists"][0]["id"]
  recommendations = sp.recommendations(seed_genres = inputG, limit = 10)
  print(recommendations)
  tracks = recommendations['tracks']
  print("tt" + str(tracks))
  link = tracks[0]["album"]['id']
  return link