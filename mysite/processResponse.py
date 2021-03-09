from . import spotifyAPI
def processRandom(response):
  link = spotifyAPI.randomMusic()
  embed = "<iframe src= \"https://open.spotify.com/embed/album/"+link +"\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"
  response = response.replace("<link>", embed, 10)
  return response
def storeInput(msg, response):
  if "We have recorded your favorite genres!" in response:
    f = open("data", "w")
    f.write(msg+"\n")
    f.close()
  elif "We have recorded your favorite artists!" in response:
    f = open("data", "w")
    f.write("\n"+msg+"\n")
    f.close()
  # else:
  #   f = open("data", "w")
  #   f.write("Tracks: "+ msg)
  #   f.close()
def processPersonal(response):
  link = ''
  if "Here is what we found for you" in response:
    f = open("data1", "r")
    s1 = f.readline()
    s2 = f.readline()
    print(s1 + s2)
    link = spotifyAPI.personalRecom(s1, s2,"")
  embed = "<iframe src= \"https://open.spotify.com/embed/album/"+link +"\" width=\"300\" height=\"80\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>"
  response = response.replace("<link>", embed, 10)
  return response