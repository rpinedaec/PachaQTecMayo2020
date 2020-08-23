from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json, requests, random, re
from pprint import pprint
# Create your views here.

from django.views import generic
from django.http.response import HttpResponse
# #PAGE_ACCESS_TOKEN = "EAAEM1jj4OgABAFBZBBWBD4yZBJsGojV1IpuOYi9tWQTYMZAAeoz2YjCyOoeu5I8cO63lrZBm1F4HDfacQT703PLZArmDJVaOB4RMxoXNFUMvmO2ptf6hB0eRPs0P8ZCHlHvkGyP7ZBhR09SZBrdh3qCBKYvgy9ZAc1wHMlVxpCdUwbfELC3pMTZBDkjEj5g9vyKu0ZD"
PAGE_ACCESS_TOKEN = 'EAAuqjonVPp4BAIrQnIELftLV6XZBQlUZCyoXFwgySjL503LjY4REqbojRSfOiMjQz02ZBHDfRl9GxoeHPdSZCWNmJq0yegNesOyq3bUhZBzPG1xxnI8TSrhuewZC16n0Go4CszUYkyHCXC3UpqYScZAmAMhbrBnY6FlZCg4Q8tgL1QZDZD'
VERIFY_TOKEN = "927248582"



# # Create your views here.
class fbMssngrView(generic.View):
    def get(self, request, *args, **kwargs):
#        return HttpResponse("Hello Martin")
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
    # The get method is the same as before.. omitted here for brevity
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)    
                    # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly. 
                    post_facebook_message(message['sender']['id'], message['message']['text'])    
        return HttpResponse()    
def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

