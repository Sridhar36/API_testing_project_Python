import requests
import json
import configparser
from utilities.configurations import *

response = requests.get(getConfig()['API']['endpoint'] + "Library/GetBook.php", params={'AuthorName': 'Rahul Shetty'})
# print(response.text)
# print(type(response.text))
# jk = json.loads(response.text)  #to parse Json string to dictionary we use json.loads. loads method is for converting
# string object to dictionary
# print(type(jk))  # this gives list., since output is in list format..
# json.loads by default converts output to list and not dict
# print(jk[0]['isbn'])

'''
instead of above we can use response.json() method provided by requests lib
this method gives response directly in json format. (instead of grabbing the texts and then using loads method.. wecan use 
this method.

This is for scenarios were we get json response from API.
'''
json_resp = response.json()
print("type of  json resp - ", type(json_resp))
print(json_resp, "\n")
print(json_resp[0]['isbn'])

# The assert keyword in Python lets you test if a condition in your code returns True,
# if not, the program will raise an AssertionError.
assert response.status_code == 200
print("response type is = ", type(response))
print("headers - ", response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# to retrieve details matching isbn 'rs1'
for book in json_resp:
    if book['isbn'] == 'rs1':
        print("book details - ", book)
        break
'''Above same operation can be done in single line using list comprehension below'''
print([book for book in json_resp if book['isbn'] == 'rs1'])
