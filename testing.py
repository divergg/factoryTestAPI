import requests

"""
endpoint = 'http://localhost:8000/clients/'

data = {
    'tel': '79994567999',
    'code': '133',
    'tag': 'some'
}

response = requests.post(endpoint, json=data)
"""

endpoint = 'http://localhost:8000/deliveries/'

data = {
    'date_of_creation': '2023-05-10 17:04',
    'message': 'Hello!',
    'code': '76'
}

response = requests.post(endpoint, json=data)
print(response.text)





