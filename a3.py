class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
cherry=parrot("cherry",10)
tom=parrot("tom",12)
print("cherry and tom are",cherry.species)
print("{}is{}ears old".format(cherry.name,cherry.age))
print("{}is{}ears old".format(tom.name,tom.age))
    