# coding=utf-8

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels.sessions import channel_session
import json

# def http_consumer(message):
#     response = HttpResponse("Hello world! You asked fo %s" % message.content['path'])
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)
@channel_session
def ws_message(message):
    jsonData = None
    try:
        jsonData = json.loads(message.content["text"],encoding = "utf-8")
    except ValueError:
        message.reply_channel.send({
                "text": json.dumps({
                "success": False,
                "message": "Invalid json request."
            })
        })
        return
    
    message.reply_channel.send({
        "text": str(json.dumps({
            "success": True,
            "message": 'Deneme mesajı'
        }))
    });
