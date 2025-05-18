items = ["bread", "pasta", "fruits", "vagetibles"]
print(items)
print(items[3])

print(items[0: 2])

# print List Element
print(items[-1])

# Add New Element in the List
items.append("butter")
print(items)
items.insert(1, 'chips')
print(items)

# Adding two list in a single list
subjects = ['CSE', 'EEE', 'MSE']
newString = items + subjects
print(newString)

# Print the of a List
print(len(newString))

# Check a items stay in the List
print('butter' in items)
print('soda' in newString)