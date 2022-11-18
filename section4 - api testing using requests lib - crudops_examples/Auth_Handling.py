import requests

url = 'https://api.github.com/user'
gitResponse = requests.get(url, verify=False, auth=('sridhar6261@gmail.com', 'B@sridhar1969'))
print(gitResponse.status_code)

# whenever you encounter SSL cert issues, we can add one more attribute verify= False
# if we give this, tho servers expect SSl certificate we are compressing it and submitting request.
