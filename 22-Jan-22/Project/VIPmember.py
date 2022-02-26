from customer import Customer

class VIPMember(Customer):
    def __init__(self, id, name, rate_of_discount=0.1, value=0, threshold=1000):
        super().__init__(id, name, rate_of_discount, value)
        self.__first_discount = rate_of_discount
        self.__second_discount = rate_of_discount + 0.05
        self.__threshold = threshold
    
    @property
    def first_discount(self):
        return self.__first_discount

    @property
    def second_discount(self):
        return self.__second_discount

    @property
    def threshold(self):
        return self.__threshold

    def get_discount(self, cost):
        if cost <= self.threshold:
            return (self.first_discount, cost*self.first_discount)
        else:
            return (self.second_discount, cost*self.second_discount)
    
    def displayCustomer(self):
        print(self.id, self.name, self.value, self.first_discount, self.second_discount, self.threshold)
    
    def setRate(self, new_rate):
        self.first_discount = new_rate
        self.second_discount = new_rate + 0.05

    @staticmethod
    def setThreshold(new_threshold):
        VIPMember.threshold = new_threshold
