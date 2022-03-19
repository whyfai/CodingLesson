from customer import Customer
from member import Member
from VIPmember import VIPMember
from destination import Destination
from service import Service
from bundle import Bundle
from booking import Booking
import sys



class Records():

    @classmethod
    def readCustomers(self):
        file = open(sys.argv[1])
        for line in file.readlines():
            if line != "\n":
                data = line.strip().split(", ")
                customer = {"id": data[0], "name": data[1], "discount": float(data[2]), "value": float(data[3])}
                if customer["id"].startswith("C"):
                    Customer(customer["id"], customer["name"], customer["discount"], customer["value"])
                elif customer["id"].startswith("M"):
                    Member(customer["id"], customer["name"], customer["discount"], customer["value"])
                elif customer["id"].startswith("V"):
                    VIPMember(customer["id"], customer["name"], customer["discount"], customer["value"])

        file.close()

    @classmethod
    def readDestinations(self):
        with open(sys.argv[2]) as file:
            for line in file.readlines():
                if line != "\n":
                    data = line.strip().split(", ")
                    Destination(data[0], data[1], int(data[2]), int(data[3]))

    @classmethod
    def readServices(self):
        with open(sys.argv[3]) as file:
            for line in file.readlines():
                if line != "\n":
                    data = line.strip().split(", ")
                    if data[0].startswith("S"):
                        Service(data[0], data[1], int(data[2]))
                    elif data[0].startswith("B"):
                        Bundle(data[0], data[1], data[2:])

    @classmethod
    def readBookings(self):
        with open(sys.argv[4]) as file:
            for line in file.readlines():
                try:
                    if line != "\n":
                        data = line.strip().split(", ")
                        Booking(data[0], data[1], int(data[2]), data[3], float(data[4]), data[5])
                except IndexError:
                    print("Booking invalid! skipping booking.")

    @staticmethod
    def findCustomer(arg):
        if arg[1].isnumeric():
            for i in Customer.customers:
                if i.id == arg:
                    return i
        else:
            for i in Customer.customers:
                if i.name == arg:
                    return i
        return None

    @staticmethod
    def findDestination(arg):
        if arg[1].isnumeric():
            for i in Destination.destinations:
                if i.id == arg:
                    return i
        else:
            for i in Destination.destinations:
                if i.name == arg:
                    return i
        return None

    @staticmethod
    def findService(arg):
        if arg[0] == "S" and arg[1].isnumeric():
            for i in Service.services:
                if i.id == arg:
                    return i
        elif arg[0] == "B" and arg[1].isnumeric():
            for i in Bundle.bundles:
                if i.id == arg:
                    return i
        else:
            for i in Service.services:
                if i.name == arg:
                    return i
            for i in Bundle.bundles:
                if i.name == arg:
                    return i
        return None

    @staticmethod
    def listCustomers():
        for i in Customer.customers:
            print(i)

    @staticmethod
    def listDestinations():
        for i in Destination.destinations:
            print(i)

    @staticmethod
    def listServices():
        for i in Service.services:
            print(i)
        for i in Bundle.bundles:
            print(i)

    @staticmethod
    def listBookings():
        print(f"{'Name':^10s}\t{'Destination':^15s}\t{'Ticket':^10s}\t{'Service':^20s}\t{'Date':^30s}")
        for i in Booking.bookings:
            print(i)
    