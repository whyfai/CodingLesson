class Booking():
    def __init__(self, customer, destination, quantity):
        self.__customer = customer
        self.__destination = destination
        self.__quantity = quantity
    
    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, new_customer):
        self.__customer = new_customer

    @property
    def destination(self):
        return self.__destination
    
    @destination.setter
    def destination(self, new_destination):
        self.__destination = new_destination

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity