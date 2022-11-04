import pytchat
import json

chat = pytchat.create(video_id='ID_LIVE_STREAMING_YOUTUBE')
while chat.is_alive():
    for c in chat.get().items:
        obj = c.json()
        obj2 = json.loads(obj)
        print(obj2['author']['name']+': '+obj2['message'])
