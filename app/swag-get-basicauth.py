from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
import logging


http_client = RequestsClient()

# api_key = 'special-key'



http_client.set_api_key('http://petstore.swagger.io/','special-key')

print http_client.authenticator.__getattribute__('host')
print http_client.authenticator.__getattribute__('api_key')

client = SwaggerClient.from_url(
    'http://petstore.swagger.io/v2/swagger.json',
    http_client=http_client
)

pet = client.pet.getPetById(petId=42).result()




print pet.name

