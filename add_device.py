import requests
import json
from get_token import get_token


# Define local varibles
url = 'https://sandboxdnac.cisco.com'
token = get_token()
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json', 'Accept-Type': 'application/json'}

# Define the device we want to add as a dictionary
new_device ={}

