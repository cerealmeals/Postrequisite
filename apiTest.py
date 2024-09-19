import requests
import json

url = "http://www.sfu.ca/bin/wcm/course-outlines?2024/fall/math/151/d100"
answer = requests.get(url)

shouldbeDic = answer.json()

print(shouldbeDic["info"]["prerequisites"])
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(answer.json())