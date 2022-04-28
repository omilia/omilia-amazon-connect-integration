
import argparse
import requests
import json

parser = argparse.ArgumentParser(description='Simple CLI tool to add numbers to your Amazon Connect Integration for Omilia.')

# Arguments
parser.add_argument('-u', 
                    '--url',
                    metavar='url',
                    type=str,
                    help='The url you created (from your API gateway)', required=True)

parser.add_argument('-k',
                    '--key',
                    type=str,
                    help='The API Key to access your api gateway', required=True)

parser.add_argument('--numbers',
                    '-n', 
                    type=str, 
                    help='Provide the list of numbers, space separated, that you would like to add to your account', 
                    nargs='*',  
                    required=True)

args = parser.parse_args()
gateway_url= args.url
api_key = args.key
pstn_numbers = args.numbers 
payload = {
    "cmd": "add_numbers",
    "numbers": pstn_numbers
}
json_payload = json.dumps(payload)
headers = {
  'x-api-key': api_key,
  'Content-Type': 'application/json'
}

response = requests.request("POST", gateway_url, headers=headers, data=json_payload)

if response.status_code == 200 : 
    print("Your numbers were added to the database!")
    print("The following numbers were added: ", pstn_numbers)
elif response.status_code ==403: 
    print("Unauthorized access. Make sure you have the correct API key!")
else: 
    print("An error might have ocurred. Check the database and lambda logs")
    print(response.text)

