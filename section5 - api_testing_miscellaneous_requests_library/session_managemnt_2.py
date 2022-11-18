import requests

se = requests.session()
se.auth = auth = ('sridhar6261','B@sridhar1969')

resp = se.get('https://api.github.com/user')
print(resp.status_code)