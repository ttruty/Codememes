import flickrapi
import random
import json


def convert_list_to_string(mlist):
    converted_list = str(mlist).strip('[]')
    converted_list = converted_list.replace('\'', '')
    return converted_list

api_key = u'e4ce59d69dd819a22c65555b0acfdb3a'
api_secret = u'e735449196b1b267'

FLICKR_PUBLIC = 'e4ce59d69dd819a22c65555b0acfdb3a'
FLICKR_SECRET = 'e735449196b1b267'
flickr = flickrapi.FlickrAPI(FLICKR_PUBLIC,FLICKR_SECRET,format='parsed-json')
random.seed()
rand_page = random.randrange(1,100000,1)
extras = 'url_t'

image_url_list = []
terms = ["animals", "places", "things", "food", "boats", "cars", "cats", "dogs", "random", "plants", "meme", "winter", "summer", "funny", "creepy", "cartoons", "gaming", "happy", "silly", "flower", "tech"]

for term in terms:
    cats = flickr.photos.search(text=term, page=rand_page, per_page=150, extras=extras)

    photos = cats['photos']

    print(photos)
    # print("Page: ",rand_page)
    #
    for image in photos['photo']:
        url = image["url_t"]
        print(url)
        image_url_list.append(url)

json_out = {"Images": convert_list_to_string(image_url_list)}

with open('images.json', 'w') as outfile:
    json.dump(json_out, outfile)


        #     self.title = image['title']
        #     try:
        #         url = image['url_o']
        #         width = image['width_o']
        #         height = image['height_o']
        #     except:
        #         try:
        #             url = image['url_l']
        #             width = image['width_l']
        #             height = image['height_l']
        #         except:
        #             try:
        #                 url = image['url_c']
        #                 width = image['width_c']
        #                 height = image['height_c']
        #             except:
        #                 pass
        # try:
        #     r = requests.get(url)
        #     self.pic = r.content
        # except:
        #     pass
