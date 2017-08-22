import requests

# Get Requests
test_case = 'PET'

get_response_pet_id = requests.get('http://petstore.swagger.io/v2/pet/42')

get_response_pet_status_pending = requests.get('http://petstore.swagger.io/v2/pet/findByStatus?status=pending')

# print get_response_pet_id.status_code
if get_response_pet_id.status_code == 200:
    print test_case +": Pass"
else:
    print test_case +": Fail"

test_case = 'ADD PET / POST'

# Post requests

url='http://petstore.swagger.io/v2/pet'
# data=''
data= {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

post_response = requests.post(url, json=data)

if post_response.status_code == 200:
    print test_case + ": Pass"
else:
    print test_case + ": Fail"
