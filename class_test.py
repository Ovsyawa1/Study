class House():
    def __init__ (self, street, number):
        self.street = street
        self.number = number
    
    def build (self):
        print("Посстроен " + self.street + " " + str(self.number))

House1 = House("Колотушкино", 33)
House1.build()