import pytesseract as tess
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request


img = Image.open('test3.png')
config = ('-l kor+eng --oem 3 --psm 11')
text = tess.image_to_string(img, config=config)
text = text.replace(" ", "")
text = text.replace('\n', "")


print(text)


def checkurl(url):
    http = urllib.request.urlopen("http://"+url)
    https = urllib.request.urlopen("https://"+url)
    originalUrl = urllib.request.urlopen(url)
    if http.status == 200:
        return "http://"+url
    elif https.status == 200:
        return "https://"+url
    elif originalUrl.status == 200:
        return url
    else:
        return ""


url = checkurl(text)
if url != "":
    driver = webdriver.Chrome(
        "/Users/yoonseonghyeon/Desktop/programming/python/selenium/chromedriver")
    driver.get(url)
