class myclass:
    def __init__(self,course,fee):
        self.course=course
        self.fee=fee
    def fun1(self):
        print(self.course,self.fee)


class myclass2(myclass):
    def __init__(self,course,fee):
        self.course=course
        self.fee=fee
    def fun3(self):
        print(self.course,self.fee)
        super().__init__("data",345)


my = myclass2("computer science",100)
my.fun3()
my.fun1()

