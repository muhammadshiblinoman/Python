def calculate_total(exp):
    total = 0
    for item in exp:
        total += item
    return total

tomExpList = [2100, 3400, 3500]
joeExpList = [200, 500, 700]

tomTotal = calculate_total(tomExpList)
joeTotal = calculate_total(joeExpList)

print('Toms total is ', tomTotal, 'Joe total is ', joeTotal)


def sum(a, b):
    print('a', a)
    print('b', b)
    total = a+b
    return total

n = sum(b = 4, a = 10)
print(n)