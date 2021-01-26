# Creating the class for the elderly person
class Patient:
    def __init__(self, name, med_occur, med_freq):
        self.name = name
        self.med_occur = med_occur
        self.med_freq = med_freq


person = Patient('agnis', ['Mon','Wed','Sat'],3)
