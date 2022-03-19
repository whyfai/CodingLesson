from customer import Customer
from member import Member
from VIPmember import VIPMember
from destination import Destination
from booking import Booking
from records import Records
from service import Service
from bundle import Bundle
import datetime
import sys
import os

class InputError(Exception):
    pass

# py -3.8 operations.py customers.txt destinations.txt services.txt bookings.txt

def menu():
    print("\nWelcome to the Melbourne bus booking system!")
    print("\n##############################################################################")
    print("You can choose from the following options:")
    print("1: Book a new trip")
    print("2: Display the current customer list")
    print("3: Display the current destination list")
    print("4: Display the current service list")
    print("5: Display the current booking list")
    print("6: Adjust the discount rate")
    print("7: Adjust the threshold price")
    print("8: Add a new destination")
    print("9: Display bookings for a customer")
    print("10: Display the most valuable customer")
    print("11: Display the most popular destination")
    print("0: Exit the program")
    print("##############################################################################\n")
    while True:
        option = int(input("Choose one option: "))
        if option >= 0 and option <= 11:
            return option

def book():
    name = input("Enter the name of the customer [e.g. Faizan]: ")
    while True:
        destination_name = input("Enter the name of the destination [e.g. Sydney, Adelaide, Brisbane]: ")
        try:
            destination = Records.findDestination(destination_name)
            if not destination:
                raise InputError("Destination not found!")
            else:
                break
        except InputError as e:
            print(e)
    while True:
        try:
            tickets = input("Enter the number of tickets [Only enter positive integers e.g. 1, 2, 3]: ")
            if not tickets.isnumeric() or int(tickets) < 1:
                raise InputError("Sorry, please enter a valid integer!")
            tickets = int(tickets)
            if tickets > destination.seatAvailable:
                raise InputError("Sorry, there are not enough seats available for this destination.")
            else:
                break
        except InputError as e:
            print(e)
    customer = Records.findCustomer(name)
    new_customer = False
    if not customer:
        new_customer = True
        while True:
            try:
                choice = input("This customer does not have a membership. Does the customer want to have a membership? [Enter y or n]: ")
                if choice.lower() not in ["y","n"]:
                    raise InputError("Sorry, please enter a valid choice!")
                else:
                    break
            except InputError as e:
                print(e)
        if choice == "y":
            while True:
                try:
                    membership = input("What kind of membership does this customer want? [Enter M or V]: ")
                    if membership.upper() == "M":
                        customer = Member("M"+str(Customer.counter), name)
                        break
                    elif membership.upper() == "V":
                        customer = VIPMember("V"+str(Customer.counter), name)
                        break
                    else:
                        raise InputError("Sorry, please enter a valid membership!")
                except InputError as e:
                    print(e)
        elif choice == "n":
            customer = Customer("C"+str(Customer.counter), name)
        else:
            raise InputError("Sorry, please enter a valid input!")
    service_price = 0
    service_name = None
    while True:
        try:
            choice = input("Would you like to buy extra services? [Enter y or n]: ")
            if choice.lower() in ["y","n"]:
                if choice.lower().startswith("y"):
                    while True:
                        try:
                            service_name = input("Enter the name of the service [e.g. Internet, Entertainment]: ")
                            service = Records.findService(service_name)
                            if not service:
                                raise InputError("Service not found!")
                            elif service.id.startswith("B"):
                                for i in service.bundle:
                                    x = Records.findService(i)
                                    service_price += x.price
                            elif service.id.startswith("S"):
                                service_price = service.price
                            if service_price == 0 and customer.id.startswith("C"):
                                raise InputError("Sorry, this service is only for members!")
                            break
                        except InputError as e:
                            print(e)
                    break
                if choice.lower().startswith("n"):
                    break
            else:
                raise InputError("Sorry, please enter a valid choice!")
        except InputError as e:
            print(e)

    subtotal = destination.price*tickets
    discount = customer.get_discount(subtotal)
    total = subtotal-discount[1]+service_price
    print("-----------------------------------------------")
    print(f"{name} books {tickets} tickets to {destination.name}.")
    print(f"{name} gets a discount of {round(float(discount[0]*100), 2)}%")
    print(f"Unit price             : {destination.price} (AUD)")
    if customer.id.startswith("V") and new_customer:
        print(f"Membership price       : 100 (AUD)")
        total += 100
        subtotal += 100
    print(f"Service price:         : {service_price} (AUD)")
    print(f"Subtotal price         : {subtotal+service_price} (AUD)")
    print(f"Total price w/ discount: {total} (AUD)")
    destination.seatAvailable -= tickets
    customer.value += total
    date = datetime.datetime.now().strftime("%d/%m/%Y %X")
    Booking(name, destination_name, tickets, service_name, round(discount[0], 3), date)

def adjust_discount():
    while True:
        try:
            discount = float(input("Enter the new discount rate [e.g. 0.1]: "))
            if discount < 0 or discount > 1:
                raise InputError("Sorry, please enter a valid discount rate!")
            else:
                break
        except InputError as e:
            print(e)
        except ValueError as e:
            print("Please enter a valid number!")
    Member.setRate(discount)

def adjust_threshold():
    while True:
        try:
            threshold = float(input("Enter the new threshold price [e.g. 100]: "))
            if threshold < 0:
                raise InputError("Sorry, please enter a valid threshold price!")
            else:
                break
        except InputError as e:
            print(e)
        except ValueError as e:
            print("Please enter a valid number!")
    VIPMember.setThreshold(threshold)

def add_destination():
    while True:
        try:
            name = input("Enter the name of the destination [e.g. Sydney, Adelaide, Brisbane]: ")
            if name in [i.name for i in Destination.destinations]:
                raise InputError("Sorry, this destination already exists!")
            break
        except InputError as e:
            print(e)
    while True:
        try:
            price = int(input("Enter the price of the destination [e.g. 100]: "))
            if price <= 0:
                raise InputError("Sorry, please enter a valid price!")
            break
        except InputError as e:
            print(e)
    Destination("D"+str(len(Destination.destinations)+1), name, price, 50)

def add_destination_menu():
    add_destination()
    while True:
        try:
            choice = input("Would you like to add another destination? [Enter y or n]: ")
            if choice.lower() not in ["y","n"]:
                raise InputError("Sorry, please enter a valid choice!")
            elif choice.lower().startswith("y"):
                add_destination()
            else:
                break
        except InputError as e:
            print(e)

def check_customer_booking():
    while True:
        try:
            name = input("Enter the name or ID of the customer: ")
            customer = Records.findCustomer(name)
            if not customer:
                raise InputError("Customer not found!")
            else:
                break
        except InputError as e:
            print(e)
    print(f"{'Name':^10s}\t{'Destination':^15s}\t{'Ticket':^10s}\t{'Service':^20s}\t{'Date':^30s}")
    for booking in Booking.bookings:
        if booking.customer == customer.id or booking.customer == customer.name:
            print(booking)

def most_valuable_customer():
    highest_value = 0
    for customer in Customer.customers:
        if customer.value > highest_value:
            highest_value = customer.value
            highest_customer = customer
    print(highest_customer)

def most_popular_destination():
    destinations = {}
    for booking in Booking.bookings:
        if booking.destination in destinations:
            destinations[booking.destination] += 1
        else:
            destinations[booking.destination] = 1
    highest_popularity = 0
    highest_destination = None
    for destination in destinations:
        if destinations[destination] > highest_popularity:
            highest_popularity = destinations[destination]
            highest_destination = destination
    print(highest_destination)

    
try:
    if len(sys.argv) == 1:
        print("Please run the program with the following command:")
        print("python3 operations.py customers.txt destinations.txt services.txt bookings.txt")
        exit()
    if len(sys.argv) == 5:
        try:
            Records.readBookings()
        except FileNotFoundError:
            print("Cannot load the booking file. Run as if there is no booking previously.")
    Records.readCustomers()
    Records.readDestinations()
    Records.readServices()
except FileNotFoundError:
    print("Error: File not found!")
    exit()

while True:
    option = menu()

    if option == 1:
        book()
    elif option == 2:
        Records.listCustomers()
    elif option == 3:
        Records.listDestinations()
    elif option == 4:
        Records.listServices()
    elif option == 5:
        Records.listBookings()
    elif option == 6:
        adjust_discount()
    elif option == 7:
        adjust_threshold()
    elif option == 8:
        add_destination_menu()
    elif option == 9:
        check_customer_booking()
    elif option == 10:
        most_valuable_customer()
    elif option == 11:
        most_popular_destination()
    else:
        with open("customers.txt", "w") as f:
            for customer in Customer.customers:
                f.write(str(customer)+"\n")
        with open("destinations.txt", "w") as f:
            for destination in Destination.destinations:
                f.write(str(destination)+"\n")
        with open("bookings.txt", "w") as f:
            for booking in Booking.bookings:
                f.write(str(booking)+"\n")
        exit()
