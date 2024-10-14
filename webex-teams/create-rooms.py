# Fill in this file with the code to create a new room from the Webex Teams exercise

# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise

import requests

access_token = 'ZWIyZDZiOTUtYjQ3Yy00MzBkLWI4NWYtODgyMmQ0OWY4M2JjNWUzOGI0MGEtYTM1_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'  
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
