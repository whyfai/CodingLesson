class Customer:
    customers = []
    counter = 12
    def __init__(self, id, name, discount=0, value=0):
        self.__id = id
        self.__name = name
        self.__discount = discount
        self.__value = value
        Customer.customers.append(self)
        Customer.counter += 1

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.discount}, {self.value}"

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def get_discount(self, cost):
        return (self.discount, cost*self.discount)

    def displayCustomer(self):
        print(self.id, self.name, self.value)