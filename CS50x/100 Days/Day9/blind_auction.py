#from gavel import logo
from replit import clear
#print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = input("What's your bid? $")


def auction(input_name, input_bid):
    parti = []
    secret_auction = {}
    secret_auction[input_name] = [input_bid]
    parti += secret_auction

    print(parti)


auction(name, bid)

while True:
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        clear()
        name = input("What is your name?: ")
        bid = input("What's your bid? $")
        auction(name, bid)
        continue

    elif answer == "no":


        break

