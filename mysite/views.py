from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import wastonAssistant
from . import userLogin

def index(request):
    
  return render(request, 'index.html')

def chat(request):
  global session
  global userName
  global response
  session = wastonAssistant.createSession()
  userName = None
  response = ""
  return render(request, 'chat.html')
  
@csrf_exempt
def regist_url(request):
    data = json.loads(request.body)
    global message
    message = data["message"]
    
    print("msg："+ message)
    return HttpResponse(request.body)
    #return render(request, 'index.html')
  
@csrf_exempt
def getResponse(request):
    global message
    global session
    global userName
    global response
    global loginStatus
    global inputUserName
    loginStatus = userLogin.checkLogin(userName)
    if loginStatus:
      response = wastonAssistant.sendMessage(message, session, userName)
    else:
      if "enter your 4-digit code" in response or "to create an account"in response or "4-digit code as your password."in response:
        response = userLogin.loginResponse(message, response, inputUserName)
      elif message == "guest":
        userName = message
        response += "\nHello, you are logged in as a <strong>"+ userName +"</strong>! What can I do for you today?\n1. Recommend Today's Top Hits\n2. Give me a personal Recomendation\n3. Recommend Anything\n4. More about Botify\n"
      else:
        response = userLogin.askLoginOrCreate(message)
        if "Is this you" in response or "Please enter your username to create an account."in response or "Do you want use name " in response:
          inputUserName = message 
      if "ogin successful" in response:
        userName = inputUserName
        response += "\nHello <strong>"+ userName +"</strong>! What can I do for you today?\n1. Recommend Today's Top Hits\n2. Give me a personal Recomendation\n3. Recommend Anything\n4. More about Botify\n"
      
    if request.is_ajax():
        return JsonResponse({"info":response})