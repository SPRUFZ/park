

# greet user and say purpose of program
print()
print()
print("Welcome to Python Adventure Park!")
print("We're going to determine your ticket prices.")
print("We'll also find out which rides you are eligible for!")
print()
#ask for all user information
guest_name = input("What is your name? ")
print()
age = int(input("How old are you? "))
print()
height = int(input("What is your height in inches? "))
print()
ticket_type = input("What type of ticket will you purchase regular or premium? ")
print()
park_member = input("Do you have a park membership? yes/no? ")
print()
with_adult = input("Are you visiting with an adult? yes/no? ")
print()
visit_time = input("What time will you be visiting the park? morning/evening? ")
print()
# define what the user age is
def calculate_admission(age):
    if age <= 4:
        return 0
    elif age <= 12:
        return 15
    elif age <= 64:
        return 30
    else:
        return 20
    # find  what the discount is based on other variables
def calculate_discount(price, park_member, visit_time):
    if park_member and visit_time == "evening":
        price -= 10
    elif park_member:
        price -= 5
    elif visit_time == "evening":
        price -= 3
    return max(price, 0)
#find price based on age and apply discount if it works
price = calculate_admission(age)
if price <= 0:
    price = 0
#ride level based on age and height
def ride_level(age, height):
    if height < 36:
        return "You are only eligible for kiddie rides."
    elif age <= 8 or height < 42:
        return "You are eligible for family rides."
    elif age <= 12 or height < 48:
        return "You are eligible for thrill rides."
    elif age <= 16 or height >= 54:    
        return "You are eligible for extreme rides."
# supervision check based on age and if they are with an adult
def check_supervision(age, with_adult):
    if age < 13 == "no":
        return "You must be accompanied by an adult to ride."
    elif age < 13 and with_adult == "yes":
        return "You can ride with adult supervision."
#ticket type check for promo
def check_ticket_type(ticket_type):
    if ticket_type == "premium":
        return "CONGRATS! You have recieved a ticket discount of 50% on your next ticket purchase."
    elif ticket_type == "regular":
        return "You dont have any promo but you do haveaccess to standard rides and attractions that you are eligible for."


#final information printout for user
print()
print("-----GUEST INFORMATION-----")
print()
print(f"USER: {guest_name}")
print(f"AGE: {age}")
print(f"HEIGHT: {height}")
print()
print("-----TICKET INFORMATION-----")
print()
print(f"TICKET TYPE: {ticket_type}")
print(f"PARK MEMBER: {park_member}")
print()
print("-----PRICE INFORMATION-----")
print()
print(f"PRICE BEFORE DISCOUNT: ${price}")
print(f"PRICE AFTER DISCOUNT: ${calculate_discount(price, park_member, visit_time)}")
print()
print("-----RIDE INFORMATION-----")
print()
print(f"RIDE LEVEL: {ride_level(age, height)}")
print(f"SUPERVISION: {with_adult}")


print()
print("-----PROMO INFORMATION-----")
print()

print(f"PROMO: {check_ticket_type(ticket_type)}")

def final_msg(age, with_adult):
    if age < 13 and with_adult == "no":
        return "You must be accompanied by an adult to ride sorry lil bro."
    elif age < 13 and with_adult == "yes":
        return "You can ride with your parents now have fun!"
    elif age >= 13 == "yes":
        return "You have access to all rides and attractions that you are eligible for."

    if park_member == "yes":
        return "You are a member."

print(f"{final_msg(age, with_adult)}")
def check_vip(ticket_type, park_member, age):
    if ticket_type == "premium" and park_member == "yes":
        return "YOU ARE A VIP MEMBER!"
    elif ticket_type == "premium" and age >= 64:
        return "YOU ARE A VIP MEMBER!"
    else:
        return "You are not a VIP member."
print(f"{check_vip(ticket_type, park_member, age)}")
print()

