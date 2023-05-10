#create wizard class model
class Wizard:

    def __init__(self,name,age,house,wand,gender,wizarding_class):
        self.name = name
        self.age = age
        self.house = house
        self.wand = wand
        self.gender = gender
        self.wizarding_class = wizarding_class
    
    def __str__(self):
        wizard_description = f'{self.name} | {self.age} | {self.house} | {self.wand}'
        return wizard_description

    def is_deatheater(self):
        is_deatheater = False
        if self.house == 'Slytherin':
            self.is_deatheater = True
        return is_deatheater
    
    def is_pureblood(self):
        return True