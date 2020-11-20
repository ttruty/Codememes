import requests
import json
import pprint

from PIL import Image
from io import BytesIO

def convert_list_to_string(list):
    converted_list = str(list).strip('[]')
    converted_list = converted_list.replace('\'', '')
    return converted_list

subscription_key = "f9f11b0236e143c99a18be026050fe8b"
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

terms = ["animals", "people", "places", "things", "food", "random", "celebs" , "winter", "summer", "fall", "sprint", "art", "vehicles", "technology", "funny", "creepy", "cartoons", "gaming", "silly", "fun", "happy", "sad", "feelings", "powerful",
         "past", "present", "future", "holiday", "party", "eat", "famous", "costume", "hero", "logo"]

# search_term = "animals"

image_list = []
for search_term in terms:
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

    params  = {"q": search_term, "license": "any", "imageType": "Clipart"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    for i in search_results['value']:
        image_list.append(i['contentUrl'])

json_out = {"Images": convert_list_to_string(image_list)}

with open('words.json', 'w') as outfile:
    json.dump(json_out, outfile)

# thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]