"""
Basic rogram to understand inheritance (subclasses)
"""

class PartyAnimal:
    def __init__(self,name):
        self.x = 0
        self.name = name
        print(self.name,"constructed")

    def party(self):
        self.x+=1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name) #initializing parent class
        self.points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()