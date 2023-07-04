class Car:
    def __init__(self, name):
        self.name = name
        print("I ran first")
 
    def product(self):
        print("I ran second")
        return ("Name: " + self.name)
 
 
C = Car('Audi R8')
print(C.product())
