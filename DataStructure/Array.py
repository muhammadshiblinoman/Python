exp = [2200,2350,2600,2130,2190]

# Difference Between First Two Month Spent
print("In feb this much extra was spent compared to jan:",exp[1]-exp[0])

# Sum of First 3 Month Spent
print("Expense for first quarter:",exp[0]+exp[1]+exp[2])

#Chec You Can Spent $2000 in any month
print("Did I spent 2000$ in any month? ", 2000 in exp)

# Add New Spent in the list
exp.append(1980)
print("Expenses at the end of June:",exp) 

# Sub $200 in month 4 or April
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp)

# Next Another Array or List in String
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))

heros.append('black panther')
print(heros)

# Remove the Black Panther in the List
heros.remove('black panther')

# Insert Black Panther in position no 3
heros.insert(3,'black panther')
print(heros)

# Insert Doctor Strange in position no 2
heros[1:3]=['doctor strange']
print(heros)

# Short in accending order in the list
heros.sort()
print(heros)