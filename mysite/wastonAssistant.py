#Watson Assitant Python Setup Tutorial:
#https://cloud.ibm.com/apidocs/assistant/assistant-v2?code=python

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from . import processResponse
def createSession():
  authenticator = IAMAuthenticator('Z5EqkvIKkkuVq6fLrQGu2RBkoeA3bbwtN95RXoSSlHGm')
  assistant = AssistantV2(
      version='2020-09-24',
      authenticator=authenticator
  )

  assistant.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/82b93eed-38b3-43f9-b7e5-fa2ce040cb0a')

  response = assistant.create_session(
      assistant_id='836d6d4e-5026-4a13-952a-e43f6832344b'
  ).get_result()
  return response

def sendMessage(msg, session, userName):
  authenticator = IAMAuthenticator('Z5EqkvIKkkuVq6fLrQGu2RBkoeA3bbwtN95RXoSSlHGm')
  assistant = AssistantV2(
      version='2020-09-24',
      authenticator=authenticator
  )
  assistant.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/82b93eed-38b3-43f9-b7e5-fa2ce040cb0a')
  print(session['session_id'])
  response = assistant.message(
      assistant_id='836d6d4e-5026-4a13-952a-e43f6832344b',
      session_id=session['session_id'],
      input={
            'message_type': 'text',
            'text': msg
      }
  ).get_result()
  print(msg)
  print(json.dumps(response))
  print(json.dumps(response['output']['generic']))
  responseString = responseMsg(msg, response, userName)
  
  return responseString

def responseMsg(msg, response, userName):
    if len(response['output']['generic']) == 0:#wrong input msg

      return "Sorry, I don't understand"
    elif len(response['output']['intents']) == 0:# record user preference
      responseString = str(json.dumps(response['output']['generic'][0]['text'], indent=2))
      responseString = responseString.replace("\\n", '<br>', 10)
      processResponse.storeInput(msg, responseString, userName)
      responseString = processResponse.processPersonal(responseString, userName)
      return responseString
    else:
      responseString = str(json.dumps(response['output']['generic'][0]['text'], indent=2))
      responseString = responseString.replace("\\n", '<br>', 10)
      print(response)
      print("intent: "+ response['output']['intents'][0]['intent'])
      intent = response['output']['intents'][0]['intent']
      if  intent == 'Anything' or intent == 'Random':
        responseString = processResponse.processRandom(responseString)
      elif intent == 'Favorite_Genres':
        responseString = processResponse.processFavoriteGenre(responseString);
      elif intent == 'Favorite_Artists':
        responseString = processResponse.processFavoriteArtists(responseString);
      elif  intent == 'top_hit':
        responseString = processResponse.processTopHit(responseString);
    return responseString