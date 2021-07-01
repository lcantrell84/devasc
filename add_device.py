import requests
import json
from get_token import get_token

# Define local varibles
url = 'https://10.10.20.85/dna/intent/api/v1/network-device'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1Zjk0YjkwMmQ1YTAxMDAwYzYyMmZiZTciLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVmOTRiOTAyZDVhMDEwMDBjNjIyZmJlNiJdLCJ0ZW5hbnRJZCI6IjVmOTRiOTAxZDVhMDEwMDBjNjIyZmJlNCIsImV4cCI6MTYyNTExMzM0NywiaWF0IjoxNjI1MTA5NzQ3LCJqdGkiOiJhYzEyOGQ5Yi1jMmVkLTRlZjUtYmRhYS1lYTM5Mzg3MmM1ZTgiLCJ1c2VybmFtZSI6ImFkbWluIn0.eqCGXQzBJgo318SQpFUs8X1T7MyKrZOAteR_AMmzlP9-Cx2EhI6lBvEfdhWmNfyAnGSl4mb93IMV_tl4i46Nzaq8uZBCtT3yM56XGlYtQmcvjs4PV4pJdPsdDvRh0d6bdNsXnJuCKljd-k8uduwokycD16qp_LKzLQP6NCVZ9IxveiIpDqUJRFUpTaH29qR0Jjg09-5TQkF2GpgfFMYcprw4TMXpp21rPB6z_wX39hdw7Zd5C9FgrXxkqFgaDkm4lcCstSfhttERN67uyr_JygI3DL0DxlvyVLnPf46g4ldcxx5dHsz6MB1N0wAZqA0uBpbT_YW4E7lrKZC8Jh4Img'
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json', 'Accept-Type': 'application/json'}

# Define the device we want to add as a dictionary
new_device = {
    "cliTransport": "ssh",
    "enablePassword": "Cisco1234!",
    "ipAddress": ["192.168.100.100"],
    "password": "Cisco1234!",
    "snmpVersion": "v3",
    "snmpAuthPassphrase": "cisco123",
    "snmpAuthProtocol": "",
    "snmpMode": "AUTHPRIV",
    "snmpPrivPassphrase": "cisco123",
    "snmpPrivProtocol": "",
    "snmpRetry": "",
    "snmpTimeout": "",
    "snmpUserName": "snmp_user",
    "snmpROCommunity": "",
    "snmpRWCommunity": "",
    "userName": "lcantrell"
}

# Define the HTTP request to add the device
response = requests.post(url=url, headers=headers, data = new_device, verify=False)

# Retrive the taskId returned by DNAC to verify that the device was added.
taskID = response.json()["response"]["taskId"]

print(taskID)