from urllib import response
import requests
import json
import jsonpath


class TestCase5:

    BASE_URL = 'https://petstore.swagger.io/'

    response_code = requests.get('https://petstore.swagger.io/v2/user/test1')
    print("API Response Data")
    print(response_code.headers)
    resp_json = response_code.json()
    print(resp_json)
