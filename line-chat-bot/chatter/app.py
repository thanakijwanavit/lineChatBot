from requests import post
import os, logging, json
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class LambdaResponse:
    isBase64Encode = False
    statusCode:int = 200
    headers:str = json.dumps({})
    body:str = json.dumps({})



class LineBot:
    """
        Line Webhook
    """
    def __init__(self, access_token, event):
        self.a_token = access_token
        self.event = event
        self.token = event['replyToken']
        self.text = event['message']['text']


    def send_reply(self):
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {'Authorization': 'Bearer ' + self.a_token}
        data = {
            "replyToken": token,
            "messages":[{
                "type":"text",
                "text": self.reply()
            }]
        }
        post(url, headers=headers, json=data)
        return True

    def reply(self):
        """ change this to what you like """
        return json.dumps(self.event)




def whResponder(input, _):
    bot = LineBot(os.environ['LINE_TOKEN'],input['body'])
    bot.send_reply

    body = input

    return LambdaResponse(
        body = json.dumps(body)
    ).to_dict()


