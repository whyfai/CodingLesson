class Booking():
    bookings = []
    def __init__(self, customer, destination, quantity, service, discount, date):
        self.__customer = customer
        self.__destination = destination
        self.__quantity = quantity
        self.__service = service
        self.__discount = discount
        self.__date = date
        Booking.bookings.append(self)
    
    def __repr__(self):
        return f"{self.customer:^10s}\t{self.destination:^15s}\t{self.quantity:^10d}\t{self.service if self.service else 'None':^20s}\t{self.date:^30s}"
    
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

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, new_service):
        self.__service = new_service
    
    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, new_date):
        self.__date = new_date
