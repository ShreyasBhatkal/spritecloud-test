from urllib import response
import requests
import json

class TestCase5:

    BASE_URL = 'https://petstore.swagger.io/'

    response_code  = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=available')
    print("API Response Data") 
    print(response_code.headers)   
    
