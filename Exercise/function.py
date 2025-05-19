def calculate_area(base, height):
    return 1/2 * base * height

base = float(input("Enter The Base: "))
height = float(input("Enter The Height: "))
area = calculate_area(base, height)
print(area)

def calculateArea(base, height, shape):
    if(shape == "rectangle"):
        return base * height
    else:
        return 1/2 * base * height

shape = input("Enter Your shape: ")
Area = calculateArea(base, height, shape)
print(Area)

for i in range(0, 4):
    for j in range(0, i):
        print("*", end="")
    print("\n")

for i in range(0, 5):
    for j in range(0, i):
        print("*", end="")
    print("\n")