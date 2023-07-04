#declaring variables
print("---declaring variables---")
var="sightspectrum"
print(var)

#valid variable name
print("---valid variable---")
variable = 1
Variable = 2
Va_ri_able = 3
_variable = 4
variable_ = 5
_variable_ = 6
print(variable,Variable,Va_ri_able)
print(_variable,variable_,_variable_)

# An integer assignment

age = 45
# A floating point

salary = 1456.8
# A string

name = "sight"
print("---integer assignment---")
print(age)
print("---floating point---")
print(salary)
print("---string---")
print(name)

# This function uses global variable s
print("---local variable---")
def f():
    s = "Welcome sightspectrum"
    print(s)
f()
# This function has a variable with
# name same as s.
print("---Global variable---")
def f():
    print(s)
# Global scope
s = "wednesday"
f()