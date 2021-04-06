import json
def checkLogin(userName):
  if (userName == None):
     return False
  
  return True

def loginResponse(msg, lastResp, userName):
  resp = lastResp
  if "enter your 4-digit code" in lastResp:
     resp =  checkCode(msg, userName)
  elif "to create an account" in lastResp:
    resp = createAccount(msg)
  elif "4-digit code as your password." in lastResp:
    if validCode(msg):
      userInfor = None
      with open('userInformation') as json_file:
        userInfor = json.load(json_file)
        
      userInfor[userName] = {}
      userInfor[userName]['genres'] = []
      userInfor[userName]['artists'] = []
      userInfor[userName]['tracks'] = []
      userInfor[userName]["code"] = msg
      
      with open('userInformation', 'w') as outfile:
         json.dump(userInfor, outfile)
      resp = "You created an account and login successful!"
    else:
      resp = "Please enter <strong>correct 4-digit </strong>code as your password."
  return resp
def askLoginOrCreate(message):
  respose = "It looks like you haven't registered an account yet.\n Do you want use name <strong>"+message+ "</strong> to create an account?"
  with open('userInformation') as json_file:
    userInfor = json.load(json_file)
    if message in userInfor and (message != "yes" or message != "no"):
      respose = "It looks like we have recorded <strong>" +message +"'s'</strong> information.\n"
      respose += "Your favorite genres are "+str(userInfor[message]["genres"]) +".\n"
      respose += "Is this you?(yes/no)"
      return respose
    elif message == "yes":
      return "please enter your 4-digit code."
    elif message == "no":
      return "Please enter your a new username to create an account."
  return respose

def validCode(message):
  if message.isdigit() and len(message) == 4:
    return True
  return False
def createAccount(message):
  respose = "Wrong input"
  with open('userInformation') as json_file:
    userInfor = json.load(json_file)
    if message == "yes":
      respose = "Please enter 4-digit code as your password."
    elif message == "no":
      respose = "Please enter your username to create an account."
    elif message in userInfor:
      respose = "user name: <strong>" +message +"</strong> already exits. \nPlease enter your username to create an account."
    else:
      respose = "Please enter 4-digit code as your password."
  return respose

def checkCode(message, userName):
  response = "Please enter 4-digit code correctly"
  with open('userInformation') as json_file:
    userInfor = json.load(json_file)
    if message == userInfor[userName]["code"]:
      response = "Login successful"
    else:
      response = "Incorrect 4-digit code, please enter your 4-digit code correctly."
  return response

def addGenres(genres, userName):
    userInfor = None
    with open("userInformation") as json_file:
        userInfor = json.load(json_file) 
    genreSet = None
    if (len(userInfor[userName]["genres"])) == 0:
        genreSet = set()
    else:
        genreSet = set(userInfor[userName]["genres"][0].split(","))
    newGenreSet = set(genres.split(","))
    genreSet.update(newGenreSet)
    genreSet = list(genreSet)
    genreString = ",".join(genreSet)
    userInfor[userName]["genres"] = [genreString]
    with open('userInformation', 'w') as outfile:
         json.dump(userInfor, outfile)
    return

def addArtists(artists, userName):
    userInfor = None
    with open("userInformation") as json_file:
        userInfor = json.load(json_file) 
    artistsSet = None
    if (len(userInfor[userName]["artists"])) == 0:
        artistsSet = set()
    else:
        artistsSet = set(userInfor[userName]["artists"][0].split(","))
    newArtistSet = set(artists.split(","))
    artistsSet.update(newArtistSet)
    artistsSet = list(artistsSet)
    artistsString = ",".join(artistsSet)
    userInfor[userName]["artists"] = [artistsString]
    with open('userInformation', 'w') as outfile:
         json.dump(userInfor, outfile)
    return

def addTracks(tracks, userName):
    userInfor = None
    with open("userInformation") as json_file:
        userInfor = json.load(json_file) 
    userInfor[userName]["tracks"].append(tracks)
    tracksSet = None
    if (len(userInfor[userName]["tracks"])) == 0:
        tracksSet = set()
    else:
        tracksSet = set(userInfor[userName]["tracks"][0].split(","))
    newTrackSet = set(tracks.split(","))
    tracksSet.update(newTrackSet)
    tracksSet = list(tracksSet)
    tracksString = ",".join(tracksSet)
    userInfor[userName]["tracks"] = [tracksString]
    with open('userInformation', 'w') as outfile:
        json.dump(userInfor, outfile)
    return