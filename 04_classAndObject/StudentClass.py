class Student:

    # initlialize method
    def __init__(self,name,roll_no,is_present,percentage):
        self.name = name
        self.roll_no = roll_no
        self.is_present = is_present
        self.percentage = percentage

    # function 
    def get_grade(self):
        if self.percentage > 80:
            return 'A'
        elif self.percentage <= 80 and self.percentage > 60:
            return 'B'
        elif self.percentage <= 60 and self.percentage > 40:
            return 'C'
        elif self.percentage <= 40 and self.percentage > 33:
            return 'D'
        else:
            return 'E'