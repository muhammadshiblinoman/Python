num = input('Enter a number: ')
num = int(num)

if num%2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# Conditional operator
print(4 > 9)
print(4 < 8 and 5 > 3)
print(4 < 9 or 9 > 10)
print(not 4 == 4)

bangli = ['samosa', 'daal', 'naan']
chinese = ['fried rise', 'pot sticker', 'egg role']
italian = ['pizza', 'pasta', 'risotto']

dish = input('Enter a dish name: ')

if dish in bangli:
    print('Bangladeshi')
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print('Italian')
else:
    print('Other')