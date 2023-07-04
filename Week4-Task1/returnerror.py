class student:
    def __init__(self, name,age):
        self.name = name
        self.age=age
        print("pass")
        return (self.age)
 
    def result(self):
        print("fail")
##        return ("Name: " + self.name)
 
 
s = student('bharani',24)
print(s.result())
