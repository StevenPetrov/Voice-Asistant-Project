from pygooglenews import GoogleNews
import json
import time

from main.tts_stt import text_to_speech, text_to_speech_en


def news_scrapper():
    gn = GoogleNews()
    top = gn.top_news()

    entries = top["entries"]
    count = 0
    for entry in entries:
        count = count + 1
        if count == 11:
            break
        text_to_speech_en(
            str(count) + ". " + entry["title"]  # + entry["published"]
        )
        time.sleep(0.25)
