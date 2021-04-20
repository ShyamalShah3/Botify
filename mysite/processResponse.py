from . import spotifyAPI
from . import userLogin
import json
def processRandom(response):
  link, trackName = spotifyAPI.randomMusic()
  embed = "<iframe src= \"https://open.spotify.com/embed/album/"+link +"\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"
  response = response.replace("<link>", embed, 10)
  return response, trackName
def processFavoriteGenre(response, userName):
  with open('userInformation') as json_file:
    userInfor = json.load(json_file)
    try:
      genres = userInfor[userName]["genres"][0]
    except:
      return "You have no favorite genre."

  response = response.replace("<genres>", genres, 10)
  return response
def processFavoriteTrack(response, userName):
  with open('userInformation') as json_file:
    userInfor = json.load(json_file)
    try:
      tracks = userInfor[userName]["tracks"][0]
    except:
      return "You have no favorite track."

  response = response.replace("<tracks>", tracks, 10)
  return response
def processFavoriteArtists(response, userName):
  with open('userInformation') as json_file:
    userInfor = json.load(json_file)
    try:
      artists = userInfor[userName]["artists"][0]
    except:
      return "You have no favorite artist."
  response = response.replace("<artists>", artists, 10)
  return response
def processTopHit(responseString):
  embed = ""
  links, trackName = spotifyAPI.topHit()
  for link in links:
      embed = embed +"<iframe src= \"https://open.spotify.com/embed/track/"+link +"\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"+"\n"
  responseString = responseString.replace("<link>", embed, 10)
  return responseString, trackName
def storeInput(msg, response, userName):
  if "We have recorded your favorite genres" in response:
    if msg == "":
      userLogin.addGenres("none", userName)
    else:
      userLogin.addGenres(msg, userName)
    # f = open("data", "w")
    # f.write(msg+"\n")
    # f.close()
  elif "We have recorded your favorite artists" in response:
    if msg == "":
      userLogin.addArtists("none", userName)
    else:
      userLogin.addArtists(msg, userName)
    # f = open("data", "a")
    # f.write(msg+"\n")
    # f.close()
  elif "Here is what we found for you" in response:
    if msg == "":
      userLogin.addTracks("none", userName)
    else:
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
  genres = "none"
  artists = "none"
  tracks = "none"
  if "Here is what we found for you" in response:
    with open("userInformation") as json_file:
        userInfor = json.load(json_file) 
    if len(userInfor[userName]['genres']) != 0:
      genres = userInfor[userName]['genres'][0]
    if len(userInfor[userName]['artists']) != 0:
       artists = userInfor[userName]['artists'][0]
    if len(userInfor[userName]['tracks']) != 0:  
      tracks = userInfor[userName]['tracks'][0]
    try:
       links, trackName = spotifyAPI.personalRecom(genres, artists,tracks)
    except:
      return "Sorry, we cannot recommend anything to you based on your provided information, \nit may because your preferences suck..."
    if "wrong artist" in links:
       return "It seems that we did not find any results based on the artists you provided."
    elif "wrong track" in links:
       return "It seems that we did not find any results based on the tracks you provided."
    if "none" in links:
      return "Please provide some information.&#128532"
  
    for link in links:
      embed = embed +"<iframe src= \"https://open.spotify.com/embed/album/"+link +"\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"+"\n"
  response = response.replace("<link>", embed, 10)
  return response, trackName