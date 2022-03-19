from customer import Customer

class Member(Customer):
    def __init__(self, id, name, rate_of_discount=0.05, value=0):
        super().__init__(id, name, rate_of_discount, value)
    
    def get_discount(self, cost):
        return (self.discount, cost*self.discount)
    
    def displayCustomer(self):
        print(self.id, self.name, self.value, self.discount)
    
    @staticmethod
    def setRate(new_rate):
        Member.discount = new_rate