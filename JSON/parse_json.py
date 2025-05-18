book = {}

book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 89745632
}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 89745632
}

import json
s = json.dumps(book)

# wtite in a file
with open("/home/noman/MyFiles/Machine Learning/Python/JSON//book.txt", "w") as f:
    f.write(s)

# read in a file
f = open("/home/noman/MyFiles/Machine Learning/Python/JSON//book.txt", "r")
s = f.read()
# print(s)

# book = json.loads(s)
# print(book)

# Print the type in a data structure
print(type(book))

print(book['bob']['phone'])

# print all record in the json
for person in book:
    print(book[person])