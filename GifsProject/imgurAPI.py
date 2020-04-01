from imgurpython import ImgurClient
import json

client_id = '2a307284fe42f2e'
client_secret = '276a4bd003c9257c9d5713f03a7ad2d3d04c95fc'

client = ImgurClient(client_id, client_secret)


def convert_list_to_string(mlist):
    converted_list = str(mlist).strip('[]')
    converted_list = converted_list.replace('\'', '')
    return converted_list

image_list = []

# Example request
for i in range(0, 50):
    print("PAGE: " + str(i))
    items = client.gallery(page=0)
    for item in items:
        image_list.append(item.link)

json_out = {"Images": convert_list_to_string(image_list)}

with open('images.json', 'w') as outfile:
    json.dump(json_out, outfile)