print("Welcome to Python Adventure Park!")
print("We're going to determine your ticket prices.")
print("We'll also find out which rides you are eligible for!")

guest_name = input("What is your name? ")
age = int(input("How old are you? "))
height = int(input("What is your height in inches? "))
ticket_type = input("What type of ticket will you purchase regular or premium? ")
park_member = input("Do you have a park membership? yes/no? ")
with_adult = input("Are you visiting with an adult? yes/no? ")
visit_time = input("What time will you be visiting the park? morning/evening? ")
def calculate_admission(age):
    if age <= 4:
        return 0
    elif age <= 12:
        return 15
    elif age <= 64:
        return 30
    else:
        return 20
def calculate_discount(price, park_member, visit_time):
    if park_member and visit_time == "evening":
        price -= 10
    elif park_member:
        price -= 5
    elif visit_time == "evening":
        price -= 3
    return price
