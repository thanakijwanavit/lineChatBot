sam build --profile villaaws &&\
sam deploy --profile villaaws --parameter-overrides LineToken=$(cat ~/.lineToken)
curl -X POST https://69xq67yud5.execute-api.ap-southeast-1.amazonaws.com/Prod/line/ -d '{"events": [{"type": "message", "replyToken": "fb384768a0e84223ac40edd36acf3442", "source": {"userId": "U4315f7179ea150fac0ad8009e695845b", "type": "user"}, "timestamp": 1601733823716, "mode": "active", "message": {"type": "text", "id": "12789384775024", "text": "hi"}}], "destination": "U7b50ae5a7e1188b777fd369683ce4175"}'
