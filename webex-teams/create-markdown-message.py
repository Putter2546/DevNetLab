# Fill in this file with the messages code from the Webex Teams exercise

import requests

access_token = 'ZWIyZDZiOTUtYjQ3Yy00MzBkLWI4NWYtODgyMmQ0OWY4M2JjNWUzOGI0MGEtYTM1_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNTAyYTJhZDAtNTc0Ny0xMWVmLWJhMDctODUyMDlkZGZiNmZj'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
