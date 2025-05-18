telephoneNumbers = {
    'tom': 12368412,
    'bob': 75215854,
    'alice': 74842325
}

telephoneNumbers['sam'] = 1234563456
print(telephoneNumbers)

# Delete in the Dictionaries
del telephoneNumbers['sam']
print(telephoneNumbers)

# print All key in the Dictionaries
for key in telephoneNumbers:
    print("key", key, "value", telephoneNumbers[key])


for u, v in telephoneNumbers.items():
    print("key", u, "value", v)

