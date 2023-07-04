print("---numeric data---")
num1 = 5
print(num1, 'is of type', type(num1))
num2 = 2.0
print(num2, 'is of type', type(num2))
num3 = 1+2j
print(num3, 'is of type', type(num3))

print("---list datatype---")
languages = ["Swift", "Java", "Python"]

print("---access list item---")
languages = ["Swift", "Java", "Python"]

# access element at index 0
print(languages[0])

# access element at index 2
print(languages[2])

print("tuple datatype")
# create a tuple
product = ('car', 'suzuki', 2)

# access element at index 0
print(product[0])

# access element at index 1
print(product[1])

print("---string datatype---")
name = 'Python'
print(name)

print("---set datatype---")
# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))

print("---Dictionary datatype---")
# create a dictionary named capital_city
capital_city = {'india': 'delhi', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)

print("---dictionary values using key---")
# create a dictionary named capital_city
capital_city = {'india': 'delhi', 'Italy': 'Rome', 'England': 'London'}

print(capital_city['india'])  # prints Kathmandu

print(capital_city['delhi'])  # throws error message


