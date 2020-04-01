import json

a_list = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeeee"]
b_list = ["11111", "22222", "33333"]



json_out = {"g-rating": convert_list(a_list), "pg": convert_list(b_list)}

with open('data.txt', 'w') as outfile:
    json.dump(json_out, outfile)

