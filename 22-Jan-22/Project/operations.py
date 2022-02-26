from customer import Customer
from member import Member
from VIPmember import VIPMember
from destination import Destination
from booking import Booking
from records import Records
from service import Service
from bundle import Bundle

class InputError(Exception):
    pass


def menu():
    print("\nWelcome to the Melbourne bus booking system!")
    print("\n##############################################################################")
    print("You can choose from the following options:")
    print("1: Book a new trip")
    print("2: Display the current customer list")
    print("3: Display the current destination list")
    print("4: Display the current service list")
    print("0: Exit the program")
    print("##############################################################################\n")
    while True:
        option = input("Choose one option: ")
        if option in ["1","2","3","0"]:
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

    subtotal = destination.price*tickets
    discount = customer.get_discount(subtotal)
    total = subtotal-discount[1]
    print("-----------------------------------------------")
    print(f"{name} books {tickets} tickets to {destination.name}.")
    print(f"{name} gets a discount of {int(discount[0]*100)}%")
    print(f"Unit price             : {destination.price} (AUD)")
    if customer.id.startswith("V") and new_customer:
        print(f"Membership price       : 100 (AUD)")
        total += 100
    print(f"Subtotal price         : {subtotal} (AUD)")
    print(f"Total price w/ discount: {total} (AUD)")
    destination.seatAvailable -= tickets
    customer.value += total
    Booking(name, destination_name, tickets)
    
try:
    Records.readCustomers()
    Records.readDestinations()
    Records.readServices()
except FileNotFoundError:
    print("Error: File not found!")
    exit()

while True:
    option = menu()

    if option == "1":
        book()
    elif option == "2":
        Records.listCustomers()
    elif option == "3":
        Records.listDestinations()
    elif option == "4":
        Records.listServices()
    else:
        break
