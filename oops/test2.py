from loguru import logger 

class labor:
    cnt = 0
    def __init__(self, temp):
        self.__temp = temp
        labor.cnt += 1

    def count_increment():
        cnt = cnt + 1

obj1 = labor("Hello")
print(obj1._labor__temp)
# print(dir(obj1))
