from customer import Customer
from member import Member
from VIPmember import VIPMember
from destination import Destination
from service import Service
from bundle import Bundle

class Records():

    @classmethod
    def readCustomers(self):
        file = open("Project/customers.txt")
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
        with open("Project/destinations.txt") as file:
            for line in file.readlines():
                if line != "\n":
                    data = line.strip().split(", ")
                    Destination(data[0], data[1], int(data[2]), int(data[3]))

    @classmethod
    def readServices(self):
        with open("Project/services.txt") as file:
            for line in file.readlines():
                if line != "\n":
                    data = line.strip().split(", ")
                    if data[0].startswith("S"):
                        Service(data[0], data[1], int(data[2]))
                    elif data[0].startswith("B"):
                        Bundle(data[0], data[1], data[2:])

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
    