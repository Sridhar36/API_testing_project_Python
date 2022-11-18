import requests

# json payload i.e request body we could say
# headers we have to pass in dictionary format
add_book_resp = requests.post("http://216.10.245.166/Library/Addbook.php", json={
    "name": "yu and the city",
    "isbn": "syouknowittmassssn",
    "aisle": "1202291919001",
    "author": "John foe"
}, headers={"Content-Type": "application/json"}, )

resp = add_book_resp.json()
print(type(resp))
print(resp)
bookId = resp['ID']
print(bookId)

# Delete Book
# we gonna get the book id from above create API and pass it in Delete API i.e Data Driven mechanism

respDelete = requests.post("http://216.10.245.166/Library/Deletebook.php", json={"ID": bookId},
                           headers={"Content-Type": "application/json"})
print(respDelete)
assert respDelete.status_code == 200
deleteResp = respDelete.json()
print(deleteResp)
assert deleteResp["msg"] == "book is successfully deleted"
