# Fill in this file with the people listing code from the Webex Teams exercise

import requests
import json

# access_token = 'ZWIyZDZiOTUtYjQ3Yy00MzBkLWI4NWYtODgyMmQ0OWY4M2JjNWUzOGI0MGEtYTM1_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'
# url = 'https://webexapis.com/v1/people'
# headers = {
#     'Authorization': 'Bearer {}'.format(access_token),
#     'Content-Type': 'application/json'
# }
# params = {
#     'email': '65070165@kmitl.ac.th'
# }
# res = requests.get(url, headers=headers, params=params)
# print(json.dumps(res.json(), indent=4))

access_token = 'ZWIyZDZiOTUtYjQ3Yy00MzBkLWI4NWYtODgyMmQ0OWY4M2JjNWUzOGI0MGEtYTM1_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jNDgwNDYzOC1kODI3LTRkNjEtOTRmNS01MTI2MDMxNzdmZjU'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
