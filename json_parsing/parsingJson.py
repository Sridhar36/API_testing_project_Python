import json

courses = '{"name": "RahuBHai", "languages": ["Python", "Java"]}'
print("this is course type : ", type(courses))

req_output = json.loads(courses)
print("type of json.loads data required courses - ", type(req_output))

print("from dict we accessed languages key and from value of it is list, so accessed using indexing \n",
      req_output['languages'][1])



