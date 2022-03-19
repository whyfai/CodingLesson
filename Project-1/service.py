class Service():
    services = []
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
        Service.services.append(self)

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.price}"
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price
