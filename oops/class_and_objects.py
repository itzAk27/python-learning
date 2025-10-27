from loguru import logger 

class labor:
    def __init__(self, first_name, last_name, wage):
        self.first_name = first_name
        self.last_name = last_name 
        self.wage = wage 
        

    def save_to_database(self):
        query = """ SELECT * FROM labors WHERE lower(first_name) = %s and lower(last_name) = %s """


obj1 = labor("Hello")
print(obj1._labor__temp)
# print(dir(obj1))
