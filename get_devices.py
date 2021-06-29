import requests
import json

# Define local varibles
url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
token ='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MDJjMGUyODE0NzEwYTIyZDFmN2UxNzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwOSJdLCJ0ZW5hbnRJZCI6IjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwMiIsImV4cCI6MTYyNDkyOTczMCwiaWF0IjoxNjI0OTI2MTMwLCJqdGkiOiJkMTc0OWMyMi05ZDY5LTQ0Y2UtOTdiZC1kNjE5ZWJmYjlmNjUiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.bKHMbjQ3f8yD5PlYCE3wQEwoT6gwHSQXC2FORIvQiPbyyMll1wclIxxqq0NRgGBanOKiBM1hOJcBkRHDF3r0cZ7vMvg_axZOYhCnvvZSUxSabPk2E-kxt0waAfP0skHYt1cUsqAlDfvND58T-cJWSDJReNROiI1do_TX30KN4CBNnTIhIik-7tA5ey-KtlFF154vetZSFzYA5oq_LN35t7pSrCdT2LT4jSZfxZ7zzG0573OqpPunZt9Nq4S7MFJKtDlEsrBrAEdSCAWceURGtU33dKSXp9jSHfdVTrVSejgBMUOjlm5hPKQbj8aueAWh88fwOuqo0q4hnCYMjIwAlQ'
headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept-Type': 'application/json'}

# REST API call to get a list of devices and return it in JSON format
response = requests.get(url=url, headers=headers)

print(json.dumps(response.json()))