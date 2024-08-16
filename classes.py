"""
A basic program to get started with classes. 
"""

class PartyAnimal:
    def __init__(self): #Method 1
        self.x=0
    
    def party(self): #Method 2
        self.x+=1
        print("So far",self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()