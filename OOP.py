# Classes
    #blueprint

class House(object):
    def __init__(self, address, owner, roof_type, roof=True):
        self.address = address
        self.owner = owner
        if roof == True:
            self.roof_type = "solar"
    def printSelf(self):
        print self.address
        print self.owner
        print self.roof_type

class Condo(House):
    def __init__(self, address, owner, roof_type, roof=True, HOA=True):
        super(Condo, self).__init__(address, owner, roof_type, roof)
        self.HOA = HOA
    def printSelf(self):
        print self.HOA
        return self

# myHouse = House("Neverland Ranch", "Michael Jackson", "solar")
# garrethHouse = House("Paisley Park", "Garreth B", "Solar")

myCondo = Condo("Graceland", "Elvis Presley", "Terra Cotta")
# print dir(myCondo)

myCondo.printSelf().printSelf()#<--- function call
#None.printSelf()

# print garrethHouse
# print myHouse

# Instance
# Methods
# Attributes
# Inheritance
# Chaining