from gavel import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = input("What's your bid? $")

def auction(input_name, input_bid):
    secret_auction ={}
    max = ''
    for key in secret_auction:
        secrect_auction[name] = bid
    for i in range(len(secret_auction)):
        max = secret_auction[0]
        if secret_auction[0] < secret_auction[1]:
            max = secret_auction[i]
    print(secret_auction)
    print(f"The winner is {name} with a bid of {max}")

while True:
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        clear()
        name = input("What is your name?: ")
        bid = input("What's your bid? $")
        continue

    elif answer == "no":
        auction(name, bid)
        break

