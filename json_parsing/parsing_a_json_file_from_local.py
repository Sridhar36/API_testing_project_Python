import json

# parsing content from json file
with open("C:\\Users\\sridh\\Downloads\\jsonfile.json") as f:
    data = json.load(f)  # json file to dictionary
    print(data)
    print(type(data))
    print(data['dashboard']['website'])
    print("\n")
    print(data['courses'][0]['details']['site'])
    # pricde of course RPA
    for course in data['courses']:
        print("looping thru -\t", course)
        if course['title'] == 'RPA':
            print("price of course is : ", course['price'])
