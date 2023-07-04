class myclass:
    def __init__(self,country,state):
        self.country=country
        self.state=state

    def fun(self):
        print(self.country,self.state)

class myclass2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.obj=myclass("tamilnadu","india")
        self.obj.fun()
    def fun1(self):
        print(self.name,self.age)
my = myclass2("virat",34)
my.fun1()
