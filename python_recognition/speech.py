import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
myText = 'how can i help you'
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("hi.wav")
playsound('/Users/yoonseonghyeon/Desktop/programming/python/hi.wav')

r = sr.Recognizer()

with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source)
    # read the audio data from the default microphone
    audio_data = r.listen(source)
   # audio_text = r.listen(source)
    #print("Recognizing...")
    # convert speech to text
    #text = r.recognize_google(audio_data, show_all=True)
    #print(text)
print(r.recognize_google(audio_data, language = "ko-KR"))
import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = '738c8b152edef25389f3d045a7f5ff75'

headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}

with open('hi.wav', 'rb') as fp:
    audio = fp.read()

res = requests.post(kakao_speech_url, headers=headers, data=audio)
