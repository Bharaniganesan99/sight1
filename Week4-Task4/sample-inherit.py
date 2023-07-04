##class myclass:
##     def __init__(self,name,age):
##          self.name=name
##          self.age=age
##     def fun1(self):
##          print(self.name,self.age)
##
##
##class myclass1:
##     def __init__(self,name,age):
##          self.name=name
##          self.age=age
##          self.obj=myclass("tamilnadu","fgsydfg")
##          self.obj.fun1()
##     def fun2(self):
##          print(self.name,self.age)
##
##          
##          
##
##class myclass3(myclass,myclass1):
##     def __init__(self,course,fee):
##          self.course=course
##          self.fee=fee
##     def fun(self):
##          print(self.course,self.fee)
####          super().__init__("bharani",24)
####          self.myclass=("bharani",24)
####          self.myclass1=("ganesan",56)
##          
####          myclass.__init__(self,"Dhoni",48)
####          myclass1.__init__(self,"sri",22)
##
##my=myclass3("Analyst",50000)
##my.fun()
##my.fun1()
##my.fun2()

class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun1(self):
        print(self.name, self.age)


class myclass1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun2(self):
        print(self.name, self.age)


class myclass3(myclass, myclass1):
    def __init__(self, course, fee):
##        super().__init__(name, age)
        self.course = course
        self.fee = fee

    def fun(self):
        print(self.course, self.fee)


my = myclass3("Analyst", 50000)
my1 = myclass1("bharani",3567)
my2 = myclass("hdwgf",736)
my.fun()
my2.fun1()
my1.fun2()
