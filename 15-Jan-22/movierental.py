# ImPoRtS
import random
import os

# sOmE vArIaBlEs
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
movies = []

# Functions
def add_movie():
    while True:
        title = input("Input Movie Title [Length Must be 3 - 20 chars]         :")
        if len(title) > 3 and len(title) < 20:
            break
    while True:
        genre = input("Input Movie Genre[Horror | Comedy | Action]             :")
        if genre in ["Horror", "Comedy", "Action"]:
            break
    while True:
        rating = int(input("Input Movie Rating[1-10]                                :"))
        if rating >= 1 and rating <= 10:
            break
    id = f"{random.choice(alphabet)}{random.choice(alphabet)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
    additional_price = {"Comedy": 3000, "Action": 4000, "Horror": 5000}
    price = len(title) * 500 + additional_price[genre]
    movies.append({"title":title, "genre":genre, "rating":str(rating), "id":id, "price":price})
    print(movies)
    print(f"Generated MovieID : {id}")
    print("\nInsert Sucess!")

def view_movie():
    if len(movies) == 0:
        print("No movie found.")
    else:
        print("Konichiwa. Here is the movies:")
        print("=======================================================================")
        print("| NO   | ID      | Title                | Genre   | Rating | Price    |")
        print("=======================================================================")
        index = 1
        for movie in movies:
            print("| {}    | {}   | {} | {}  | {} | {} |".format(index, movie["id"], movie["title"]+(" "*(20-len(movie["title"]))), movie["genre"], movie["rating"]+(" "*(6-len(movie["rating"]))), str(movie["price"])+(" "*(8-len(str(movie["price"]))))))
            index += 1
        print("=======================================================================")
        print("どうもありがとうございます all payments are non refundable")

def rent_movie():
    if len(movies) == 0:
        print("No movie found.")
    else:
        view_movie()
        while True:
            index = int(input(f"Choose Movie index [1-{len(movies)}]:"))
            if index >= 1 and index <= len(movies):
                break
        price = movies[index-1]["price"]
        while True:
            money = int(input(f"Input Money to Rent [MIN {price}]: "))
            if money >= price:
                break
        movies.pop(index-1)
        print(f"Pay Rent Successful with {money-price} Change")

# Stuff
while True:
    print("""



    ================
    MOVIE   RENTAL
    ================
    1. Add new Movie
    2. View Movie (Sort by Title Ascending)
    3. Rent Movie
    4. EXIT
    >>
    """)

    option = input("")

    if option == "1":
        add_movie()

    if option == "2":
        view_movie()

    if option == "3":
        rent_movie()

    if option == "4":
        print("ok bye lol")
        break

print("Thanks for using Faizan's Movie Reental Service. Please come again! weeeeeeeeeeeeee")