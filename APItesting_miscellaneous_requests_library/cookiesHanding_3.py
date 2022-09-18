'''
Cache in a website & usage-
cookie: will see what is the visit month. if the visit month is recent and we dont have any site changes after that month
we will load website from whatever cache they have.
if we have site updates, we bring from real server

if you want to send cookies, you will need to send it in dictionary format
'''
import requests

cookie = {'visit-month': 'July'}
resp = requests.get("https://rahulshettyacademy.com/", cookies=cookie)
print(resp.status_code)

# se = requests.session(cookie)
# se.cookies.update()
binCookieResp = requests.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(binCookieResp.text)  # .text gives json

se = requests.session()
se.cookies.update(cookie)
binCookieRespWithse = se.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(binCookieRespWithse.text)  # .text gives json
