class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def fun(self):
        print(self.name,self.id)
class student1(student):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def fun1(self):
        print(self.name,self.id)
    
s=student1("bharani",123)
s.fun1()
s.fun()
