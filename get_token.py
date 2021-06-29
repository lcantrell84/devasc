import requests
import json

# Define local varibles
url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
auth = ("devnetuser", "Cisco123!")
headers = {'Content-Type': 'application/json', 'Accept-Type': 'application/json'}

def get_token():
    """Method used to get and return an X-Auth-Token for DNAC"""
    response = requests.post(url=url, auth=auth, headers=headers)
    token = response.json()['Token']
    return token

def main():
    token = get_token()
    print(token)

if __name__ == "__main__":
    main()