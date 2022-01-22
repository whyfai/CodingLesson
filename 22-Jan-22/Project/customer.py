class Customer:
    def __init__(self, id, name, value=0):
        self.__id = id
        self.__name = name
        self.__value = value

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
    def value(self):
        return self.__value
    
    @value.setter
    def id(self, new_value):
        self.__value = new_value

    def get_discount(self, cost):
        pass

    def displayCustomer(self):
        print(self.id, self.name, self.value)