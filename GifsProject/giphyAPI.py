import giphy_client
import json

import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint


def convert_list_to_string(list):
    converted_list = str(list).strip('[]')
    converted_list = converted_list.replace('\'', '')
    return converted_list

ratings = ["g", "pg", "pg-13", "r"]
terms = ["animals", "people", "places", "things", "food", "boats", "cars", "cats", "dogs", "random", "celebs" , "plants", "meme", "winter", "summer", "funny", "creepy", "cartoons", "gaming", "happy", "silly"]
# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'XtbAmaclmp3f1hk6WyOb8zo6fIETIB6s' # str | Giphy API Key.
q = 'random' # str | Search query term or prhase.
limit = 100 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'r' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
g_list = []
pg_list = []
pg_13_list = []
r_list = []

for rating in ratings:
    rating = rating
    for term in terms:
        q = term
        try:
            # Search Endpoint
            api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
            # pprint(api_response)
            gif = api_response.data
            for g in gif:
                if rating == "g":
                    g_list.append(g.images.fixed_height_small.url)
                elif rating == "pg":
                    pg_list.append(g.images.fixed_height_small.url)
                elif rating == "pg-13":
                    pg_13_list.append(g.images.fixed_height_small.url)
                elif rating == "r":
                    r_list.append(g.images.fixed_height_small.url)
                else:
                    print("error in rating code")
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

json_out = {"G-Rated": convert_list_to_string(g_list),
            "PG": convert_list_to_string(pg_list),
            "PG-13": convert_list_to_string(pg_13_list),
            "R": convert_list_to_string(r_list)}

with open('words.json', 'w') as outfile:
    json.dump(json_out, outfile)