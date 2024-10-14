# Fill in this file with the authentication code from the Webex Teams exercise

import requests
import json

access_token = 'ZWIyZDZiOTUtYjQ3Yy00MzBkLWI4NWYtODgyMmQ0OWY4M2JjNWUzOGI0MGEtYTM1_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'

url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
