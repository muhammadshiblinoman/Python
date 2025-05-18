exp = [2340, 2500, 3100, 2980, 2100]
total = 0
# for item in exp:
#     total += item

for i in range(0, 5):
    print('Month', (i+1), 'Expense: ', exp[i])
    total += exp[i]

print(total)


key_location = 'chair'
locations = ['grage', 'living room', 'chair', 'closet']
for i in locations:  # For Each Loop
    if(i == key_location):
        print('key is founded')
        break
    else:
        print('key is not founded')

i = 1
while i <= 5:
    print(i)
    i = i + 1

