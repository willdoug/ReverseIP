import requests
import json
import sys

#mode of use: 
#python3 SecurityTrails.py site.com
domain=sys.argv[1] 

print("\n")

url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains?children_only=false&include_inactive=true"
headers = {
    "accept": "application/json",
    "APIKEY": "*******-******************" #put your apiKey here
}

response = requests.get(url, headers=headers)

data = response.json()

count = 0
for subdomains in data['subdomains']:
    print(subdomains + "." + domain)
    with open(domain + '_security_trails.txt', 'a') as f:
        f.writelines(subdomains + "." + domain + "\n")
        f.close()
    count +=1

print("\nTotal of Subdomains: " + str(count))
