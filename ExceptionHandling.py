num1 = input("Enter number1: ")
num2 = input("Enter number2: ")

try:
    div = int(num1) / int(num2)
except Exception as e:
    print('Exception occured: ', e)
    div = None
print(div)