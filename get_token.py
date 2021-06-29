import requests

# Define local varibles
url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
headers = {'Auhorizatoin': 'basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='}

def get_token():
    """Method used to get and return an X-Auth-Token for DNAC"""
    response = requests.post(url=url, headers=headers)
    token = json.dumps(response.json([Token]))
    print(token)
    return token