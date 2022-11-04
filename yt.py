import pytchat

chat = pytchat.create(video_id="ID_LIVE_STREAMING_YOUTUBE")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
