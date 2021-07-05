import requests

def meraki_get(resource):
    """
    Take a specific REST resource and return the JSON-romatted body text.
    """
    # Basic veriables needed
    api_path = "https://dashboard.meraki.com/api/v0"
    headers = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    # Assemble the complete URL by appending the resource to the API Path.
    # Issue an HTTP GET using proper authentication headers.
    get_resp = requests.get(f"{api_path}/{resource})", headers=headers)

    # IF status code >= 400, raise HTTPError.
    get_resp.raise_for_status()

    # HTTP GET request succeeded; return body data
    return get_resp.json()

def main():
    """
    Exectuion begins here.
    """

    # Get the list of organizations from the sandbox
    orgs = meraki_get("organizations")
    print("organizations discoverd:")

    # Debugging line; pretty-print JSON to see structure
    # import jason; print(json.jumps(orgs, indent=s))

    # Iterate over each org. This loop does double-duty. It prints out each,
    # discovered organization, but also performs a linear search for the
    # DevNet ID. If the ID is found, it is stored in the variable above.
    devnet_id = 0
    for org in orgs:
        print(f"ID: {org['id']:<6}   Name:  {org['name']}")
        if "devnet" in org["name"].lower():
            devnet_id = org["id"]
    
    # If the DevNet ID has been defined
    # then we will perform another GET request to collect the DevNet
    # networks. If the DevNet ID hasn't been defined, then we didn't find it
    # so don't try to dig deeper into that organization.
    if devnet_id:
        networks = meraki_get(f"organizations/{devnet_id}/networks")

        # Debugging line; pretty-prent JSON to see structure
        # import json; print(json.dumps(networks, indent=2))

        # Print out the networks along with their network IDs
        print(f"\nNetworks seen for DevNet org ID {devnet_id}:")

        # Print each network discovered and search for the Devnet-specific one.
        # Once found, store that network ID for later
        devnet_network = ""
        for network in networks:
            print(f"Network ID: {networkd['id']}   Name:  {network['name']}")
            if "devnet"in network["name"].lower():
                devnet_network = network["id"]

        # If we found the DevNet network ...
        if debnet_network:
            # Get the devices from the DevNet network
            devices = meraki_get(f"networks/{devnet_network}/devices")

            # Debugging line; pretty-print JSON to see structure
            # import json; print(json.dumps(devices, indent=2))

            # Print out the networks along with their network IDs 
            print(f"\nDevices seen on DevNet network {devnet_network}:")

            # Print the hardware model and LAN-side IP address on each device
            for device in devices:
                print(f"Model: {device['model']:<8}    IP:   {device['lanIp']}")


if __name__ == "__main__":
    main()
