import requests
from sqlalchemy import null

profile_name = 'profile1'

#data = {'profile_name' : profile_name}


# response = requests.post('http://127.0.0.1:5000/user_profile/'+profile_name, json= data, headers=headers)
# print(response,response.content)

# response = requests.get('http://127.0.0.1:5000/user_profile/'+profile_name)
# print(response, response.content)
#
# response = requests.delete('http://127.0.0.1:5000/user_profile/'+profile_name, json= data, headers=headers)
# print(response,response.content)
#

data = {
    "id": None,
    "name": 'Bucatarie',
    "profile_name": 'profile1'
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post('http://127.0.0.1:5000/room/1', json= data, headers=headers)
print(response,response.content)

