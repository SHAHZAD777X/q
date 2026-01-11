class vehicle:
    def __init__(self,name,max_speed,mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage
obj1=vehicle("School Volo",188,12)
print(obj1.name,obj1.max,obj1.max_speed,obj1.mileage)
obj2=vehicle("audi",248,18)
print(obj2.name,obj2.max,obj2.max_speed,obj2.mileage)
obj3=vehicle("bmw",268,15)
print(obj3.name,obj3.max,obj3.max_speed,obj3.mileage)