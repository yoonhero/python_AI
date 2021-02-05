import requests
import pyglet
from playsound import playsound

# good_song = pyglet.media.load("/Users/yoonseonghyeon/Desktop/programming/python/good.wav")
#bad_song = pyglet.media.load("/Users/yoonseonghyeon/Desktop/programming/python/bad.wav")
# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "dd3af340-bc38-11ea-9a09-91ae421c43a0ae2e7ced-d140-40eb-84fc-7d9b297c0473"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify(input("word: "))

label = demo["class_name"]
confidence = demo["confidence"]
if label == "good":
    playsound('/Users/yoonseonghyeon/Desktop/programming/python/good.wav')
    #good_song.play()
    #pyglet.app.run()
elif label == "bad":
    playsound('/Users/yoonseonghyeon/Desktop/programming/python/bad.wav')

    #bad_song.play()
    #pyglet.app.run()

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))