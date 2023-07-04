

class myclass:
    def __init__(self,course,fee):
        self.course=course
        self.fee=fee
    def fun1(self):
        print(self.course,self.fee)

class myclass1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun2(self):
        print(self.name,self.age)

class myclass2(myclass1,myclass):
    def __init__(self,course,fee):
        self.course=course
        self.fee=fee
    def fun3(self):
        print(self.course,self.fee)
        myclass.__init__(self,"biology",345)
        myclass1.__init__(self,"bharani",24)


my = myclass2("computer science",100)
my.fun3()
my.fun1()
my.fun2()
