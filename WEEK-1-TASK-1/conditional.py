print("---if---")
a = 33
b = 200
if b > a:
  print("b is greater than a")
print("---elif---")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print("---else---")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("---conditional statement using python---")
def sign(num):
    if num < 0:
        return ("Negative")

    if num > 0:
        return ("Positive")