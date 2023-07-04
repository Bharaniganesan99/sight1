##class bank:
##    def __init__(self):
##        self.__value=10
##    def bharani(self):
##        print("value:",self.__value)
##
##obj=bank()
##obj.bharani()

##class Taxi:
##
##    def __init__(self, model, capacity, variant):
##        self.__model = model      
##        self.__capacity = capacity
##        self.__variant = variant
##
##    def getModel(self):          
##        return self.__model
##
##    def getCapacity(self):        
##        return self.__capacity
##
##    def setCapacity(self, capacity):  
##        self.__capacity = capacity
##
##    def getVariant(self):        
##        return self.__variant
##
##    def setVariant(self, variant):  
##        self.__variant = variant
##
##class Vehicle(Taxi):
##
##    def __init__(self, model, capacity, variant, color):
##         
##        super().__init__(model, capacity, variant)
##        self.__color = color
##
##    def vehicleInfo(self):
##        return self.getModel() + " " + self.getVariant() + " in " + self.__color + " with " + self.getCapacity() + " seats"
##
##
##
##v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
##print(v1.vehicleInfo())
##print(v1.getModel())

class Taxi:

    def __init__(self, model, capacity, variant):
        self.__model = model      
        self.__capacity = capacity
        self.__variant = variant

    def getModel(self):          
        return self.__model

    def getCapacity(self):        
        return self.__capacity

    def setCapacity(self, capacity):  
        self.__capacity = capacity

    def getVariant(self):        
        return self.__variant

    def setVariant(self, variant):  
        self.__variant = variant

class Vehicle(Taxi):

    def __init__(self, model, capacity, variant, color):
         
        super().__init__(model, capacity, variant)
        self.__color = color

    def vehicleInfo(self):
        print(self.getModel())
        return self.getVariant() + " in " + self.__color + " with " + self.getCapacity() + " seats"



v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
print(v1.vehicleInfo())
v1.getModel()

