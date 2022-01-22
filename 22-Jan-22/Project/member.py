from numpy import rate
from customer import Customer

class Member(Customer):
    def __init__(self, id, name, value, rate_of_discount=5):
        super().__init__(id, name, value)
        self.__rate_of_discount = rate_of_discount

    @property
    def rate_of_discount(self):
        return self.__rate_of_discount

    @rate_of_discount.setter
    def rate_of_discount(self, new_discount):
        self.__rate_of_discount = new_discount
    
    def get_discount(self, cost):
        return (self.rate_of_discount/100, cost*(self.rate_of_discount/100))
    
    def displayCustomer(self):
        print(self.id, self.name, self.value, self.rate_of_discount)
    
    @staticmethod
    def setRate(new_rate):
        Member.rate_of_discount = new_rate