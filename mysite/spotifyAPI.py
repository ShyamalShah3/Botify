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
  trackName = tracks[0]["name"]
  return link, trackName
def topHit():
  sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials ("5f75bd64fe6742598b2d4650d401e9fe", "bf777b8578dd4f55b25b31f768eec9c2"))
  topHitPlayList = sp.playlist_tracks("37i9dQZF1DXcBWIGoYBM5M", limit = 50)
  track_ids = []
  track_ids.append(topHitPlayList["items"][0]["track"]["id"])
  second = random.randint(1,49)
  track_ids.append(topHitPlayList["items"][second]["track"]["id"])
  third = random.randint(3,49)
  if (second == third):
    third = third - 1
  track_ids.append(topHitPlayList["items"][third]["track"]["id"])
  trackName = topHitPlayList["items"][0]["track"]['name'] + "," + topHitPlayList["items"][second]["track"]['name']+","+topHitPlayList["items"][third]["track"]['name']
  return track_ids, trackName

def personalRecom(genres, artists, tracks):
  sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials ("5f75bd64fe6742598b2d4650d401e9fe", "bf777b8578dd4f55b25b31f768eec9c2"))
  # genres = genres.strip('\n')
  # artists = artists.strip('\n')
  # tracks = tracks.strip('\n')
  inputG = list(genres.split(",")) 
  listArtists = list(artists.split(",")) 
  listTracks = list(tracks.split(","))
  inputA = []
  inputT = []
  try:
    if artists != "none":
      for i in range(len(listArtists)):
        searchA = sp.search(q = listArtists[i], limit = 1)
        inputA.append(searchA["tracks"]["items"][0]["artists"][0]["id"])
  except:
    return "wrong artist"
  try:
    if tracks != "none":
      for j in range(len(listTracks)):
        searchA = sp.search(q = listTracks[j], limit = 1)
        inputT.append(searchA["tracks"]["items"][0]["id"])
  except:
    return "wrong track"
  none = 0
  if genres == "none":
    inputG = None
    none +=1
  if artists == "none":
    inputA = None
    none +=1
  if tracks == "none":
    inputT = None
    none +=1
  print(none)
  if none ==3 :
    return "none", None
#, seed_genres = inputG
  # if artists == "none" and tracks != "none":
  #   recommendations = sp.recommendations(seed_genres = inputG, seed_tracks=inputT, limit = 10)
  # elif artists != "none" and tracks == "none":
  #   recommendations = sp.recommendations(seed_artists = inputA,seed_genres = inputG, limit = 10)
  # elif artists == "none" and tracks == "none":
  #   recommendations = sp.recommendations(seed_genres = inputG, limit = 10)
  # else:
  recommendations = sp.recommendations(seed_artists = inputA ,seed_genres = inputG, seed_tracks=inputT, limit = 10)
  print(recommendations)
  #print(recommendations)
  tracks = recommendations['tracks']
  #print("tt" + str(tracks))
  #link = tracks[0]["album"]['id']
  links = []
  trackName = ""
  for i in range(9):
    links.append(tracks[i]["album"]['id'])
    trackName += tracks[i]['name']
    trackName += ","
  return links, trackName
