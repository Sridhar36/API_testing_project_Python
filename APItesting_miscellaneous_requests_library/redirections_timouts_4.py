'''
if there is any redirection from one website to another, then fist we get 302 first then 200
If you check the API response, then it will show only the final response i.e 200

how will you check the redirection?
what if requirement is like no redirection should happen?

allow_redirects=False - if we pass this, it will stop at the first response only.
timeout = 5 - Wait for 5 seconds before getting the API response. In real time projects API give slow response due to load.
'''

import requests

# http://rahulshettyacademy.com
# 'visit-month'
cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
# 301,200
print(response.history)
print(response.status_code)
