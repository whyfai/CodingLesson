from customer import Customer

class VIPMember(Customer):
    def __init__(self, id, name, value, rate_of_discount=10, threshold=1000):
        super().__init__(id, name, value)
        self.__first_discount = rate_of_discount
        self.__second_discount = rate_of_discount + 5
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
            return (self.first_discount/100, cost*(self.first_discount/100))
        else:
            return (self.second_discount/100, cost*(self.second_discount/100))
    
    def displayCustomer(self):
        print(self.id, self.name, self.value, self.first_discount, self.second_discount, self.threshold)
    
    def setRate(self, new_rate):
        self.first_discount = new_rate
        self.second_discount = new_rate + 5

    @staticmethod
    def setThreshold(new_threshold):
        VIPMember.threshold = new_threshold
