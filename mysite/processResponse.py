from . import spotifyAPI
from . import userLogin
import json
def processRandom(response):
  link = spotifyAPI.randomMusic()
  embed = "<iframe src= \"https://open.spotify.com/embed/album/"+link +"\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"
  response = response.replace("<link>", embed, 10)
  return response
def processFavoriteGenre(response):
  f = open("data", "r")
  geners = f.readline()
  f.close()
  response = response.replace("<genres>", geners, 10)
  return response
def processFavoriteArtists(response):
  f = open("data", "r")
  geners = f.readline()
  artists = f.readline()
  f.close()
  response = response.replace("<artists>", artists, 10)
  return response
def processTopHit(responseString):
  response = "<iframe src= \"https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"
  return response
def storeInput(msg, response, userName):
  if "We have recorded your favorite genres!" in response:
    userLogin.addGenres(msg, userName)
    # f = open("data", "w")
    # f.write(msg+"\n")
    # f.close()
  elif "We have recorded your favorite artists!" in response:
    userLogin.addArtists(msg, userName)
    # f = open("data", "a")
    # f.write(msg+"\n")
    # f.close()
  elif "Here is what we found for you" in response:
    userLogin.addTracks(msg, userName)
    # f = open("data", "a")
    # f.write(msg+"\n")
    # f.close()
  # else:
  #   f = open("data", "w")
  #   f.write("Tracks: "+ msg)
  #   f.close()
def processPersonal(response, userName):
  embed = ""
  if "Here is what we found for you" in response:
    with open("userInformation") as json_file:
        userInfor = json.load(json_file) 
    genres = userInfor[userName]['genres'][0]
    artists = userInfor[userName]['artists'][0]
    tracks = userInfor[userName]['tracks'][0]
    try:
       links = spotifyAPI.personalRecom(genres, artists,tracks)
    except:
      return "Sorry, we cannot recommend anything to you based on your provided information, \nit may because your favorite genre is piano, but your favorite artist is a rapper."
    if "wrong artist" in links:
       return "you provided wrong artists"
    elif "wrong track" in links:
       return "you provided wrong tracks"
    if "none" in links:
      return "Please provide some information.&#128532"
  
    for link in links:
      embed = embed +"<iframe src= \"https://open.spotify.com/embed/album/"+link +"\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"+"\n"
  response = response.replace("<link>", embed, 10)
  return response