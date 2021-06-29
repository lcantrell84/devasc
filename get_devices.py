import requests
import json
from get_token import get_token

# Define local varibles
url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
token = get_token()
headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept-Type': 'application/json'}

# REST API call to get a list of devices and return it in JSON format
response = requests.get(url=url, headers=headers)

print(json.dumps(response.json()))