from bravado.client import SwaggerClient

client = SwaggerClient.from_url('http://petstore.swagger.io/v2/swagger.json')
pet = client.pet.getPetById(petId=42).result()

print pet.name

