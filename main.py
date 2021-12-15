MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}
money = 0
state = True
fund = 0



def report():
    global money
    resources['money'] = money
    print(resources)


def choose_drink():
    choice = input("Please choose a drink:\n espresso, latte or cappuccino:  ").lower()
    return choice


def turn_off():
    global state
    if want_coffee == "off":
        print("Come back for more coffee!")
        state = False


def check_resources(drink):
    global state
    global resources
    for keys, values in MENU[drink]["ingredients"].items():
        if values >= resources[keys]:
            print(f"Sorry there is not enough {keys}")
            state = False



def insert_coins():
    global fund
    print("Please insert coins")
    quarters = int(input("Please insert quarters: "))
    dimes = int(input("Please insert dimes: "))
    nickles = int(input("Please insert nickles: "))
    pennies = int(input("Please insert pennies: "))
    fund = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return fund


def check_costs(drink):
    if fund >= MENU[drink]["cost"]:
        return True
    else:
        return False


def if_change(drink):
    global state
    global money
    if fund > MENU[drink]["cost"]:
        change = fund - MENU[drink]["cost"]
        print(f"Here is ${change} change")
        money += MENU[drink]["cost"]

    elif fund == MENU[drink]["cost"]:
        money += MENU[drink]["cost"]

    else:
        print("Sorry that's not enough money. Money refunded")
        state = False


def make_coffee(drink):
    global resources
    for ingredients, value in MENU[drink]["ingredients"].items():
        if ingredients not in resources:
            continue
        else:
            resources[ingredients] -= value
    return resources


while state:

    want_coffee = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if want_coffee == "report":
        report()
    elif want_coffee == "off":
        turn_off()
    elif want_coffee in "espresso, latte, cappuccino".lower():

        check_resources(want_coffee)
        insert_coins()
        if_change(want_coffee)
        make_coffee(want_coffee)
        print(f"Here is your {want_coffee}, enjoy")
print("thanks for visiting, please come back later")











