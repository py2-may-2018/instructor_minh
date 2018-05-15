#class - Blueprint of a type of object
class House(object):
    def __init__(self, owner, address, rooms, size, price):
        self.owner = owner
        self.address = address
        self.rooms = rooms
        self.size = size
        self.price = price
        if price > 500000:
            self.tax_rate = .035
        else:
            self.tax_rate = .04
    def printMe(self):
        print self.owner
        print self.address
        print self.rooms
        print self.size
        print self.price
        print self.tax_rate
    
    # def __str__(self):
    #     return self.owner + " " + self.address
class Condo(House):
    def __init__(self, owner, address, rooms, size, price, hoa_dues):
        super(Condo, self).__init__(owner, address, rooms, size, price)
        self.hoa_dues = hoa_dues
    def printMe(self):
        super(Condo, self).printMe()
        print self.hoa_dues
        return self
        

#instances - actual copy of that class
myHouse = Condo("Minh nguyen", "Lynnwood, WA", 4, 1500, 300000, 150)
# print myHouse
richardHouse = Condo("Richard Rosen", "Richmond, VA",  10, 4000, 700000, 200)
richardHouse.owner = "Richard ross"
print richardHouse
#     richardHouse
# richardHouse.printMe().printMe().printMe()
#richarHouse.printMe()
#richardHouse.printMe()

# myHouse.printMe(5)
# print richardHouse
#attributes - properties of your class
#methods - functions of your class
#inheritance
#chaining




# print "Hello my name is {}".format("Minh")

# x = [] #list
# x.append()
# x.pop

# z = []
# z.append


# y = {} #dict
# print dir(y)
# y["name"] = 