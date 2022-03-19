class Destination():
    destinations = []
    def __init__(self, id, name, price, seatAvailable):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__seatAvailable = seatAvailable
        Destination.destinations.append(self)

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.seatAvailable}"

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
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def seatAvailable(self):
        return self.__seatAvailable

    @seatAvailable.setter
    def seatAvailable(self, new_seatAvailable):
        self.__seatAvailable = new_seatAvailable
