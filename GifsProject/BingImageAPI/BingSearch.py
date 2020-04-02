import requests
import json
import pprint

from PIL import Image
from io import BytesIO

subscription_key = "##################"
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

terms = ["animals", "people", "places", "things", "food", "random", "celebs" , "winter", "summer", "art", "vehicles", "technology", "funny", "creepy", "cartoons", "gaming", "silly"]
# search_term = "animals"

for search_term in terms:
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

    params  = {"q": search_term, "license": "any", "imageType": "Clipart"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    for i in search_results['value']:
        print(i['contentUrl'])

# thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]