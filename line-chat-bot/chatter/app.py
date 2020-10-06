from requests import post
import os, logging, json
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi(os.environ['LINE_TOKEN'])
GROUP_ID = 'C9ba1d024ed36979222a2a2a8f67cfc9a'
def lineLog(message:str):
  line_bot_api.push_message(
   GROUP_ID,
   TextSendMessage(text = f'{message}'))

@dataclass_json
@dataclass
class LambdaResponse:
    isBase64Encode = False
    statusCode:int = 200
    body:str = json.dumps({})




class LineBot:
    """
        Line Webhook
    """
    def __init__(self, access_token, event):
        self.a_token = access_token
        self.event = event
        #lineLog(f'event is {event}')
        self.token = event['replyToken']
        self.text = event['message']['text']


    def send_reply(self):
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {'Authorization': 'Bearer ' + self.a_token}
        data = {
            "replyToken": self.token,
            "messages":[{
                "type":"text",
                "text": self.reply()
            }]
        }
        result = post(url, headers=headers, json=data)
        #lineLog(f'result is {repr(result)}')
        return True

    def reply(self):
        """ change this to what you like """
        return json.dumps(self.event)




def whResponder(input, _):
    try:
      bot = LineBot(os.environ['LINE_TOKEN'],json.loads(input['body'])['events'][0])
      bot.send_reply()
      return LambdaResponse(
          body = json.dumps(input['body'])
      ).to_dict()
    except Exception as e:
      logging.error(repr(e))
      lineLog(repr(e))
      return LambdaResponse(
          body = f"{repr(e)}"
      ).to_dict()

def chatter(input, _):
    try:
      bot = LineBot(os.environ['LINE_TOKEN'],json.loads(input['body'])['events'][0])
      bot.reply = lambda x: x
      bot.send_reply()
      return LambdaResponse(
          body = json.dumps(input['body'])
      ).to_dict()
    except Exception as e:
      logging.error(repr(e))
      lineLog(repr(e))
      return LambdaResponse(
          body = f"{repr(e)}"
      ).to_dict()


