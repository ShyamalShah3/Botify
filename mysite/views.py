from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import wastonAssistant

def index(request):
    
  return render(request, 'index.html')

def chat(request):
  global session
  session = wastonAssistant.createSession()
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
    response = wastonAssistant.sendMessage(message, session)
    if request.is_ajax():
        return JsonResponse({"info":response})