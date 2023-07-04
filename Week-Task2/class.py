class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, my name is", self.name, "and I am", self.age, "years old.")


person1 = Person("Bharani", 25)
##print(person1.name)  
##print(person1.age) 
person1.introduce()

