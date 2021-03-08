import math

water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
close = 1
resources = 1

def check_resources(coffee_type):

    global water
    global coffee_beans
    global money
    global milk
    global disposable_cups
    global resources

    if coffee_type == 1:
        ch_water = 250
        ch_milk = 0
        ch_coffee_beans = 16
    elif coffee_type == 2:
        ch_water = 350
        ch_milk = 75
        ch_coffee_beans = 20
    elif coffee_type == 3:
        ch_water = 200
        ch_milk = 100
        ch_coffee_beans = 12
    
    if water < ch_water:
        resources = 0
        print("Sorry, not enough water!")
    elif milk < ch_milk:
        resources = 0
        print("Sorry, not enough milk!")
    elif coffee_beans < ch_coffee_beans:
        resources = 0
        print("Sorry, not enough coffe beans!")
    else:
        print("I have enough resources, making you a coffee!")
        resources = 1
    


def printer():
    print()
    print("The coffe machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")

def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choose = input()
    if choose != "back":
        choose = int(choose)
    
    global water
    global coffee_beans
    global money
    global milk
    global disposable_cups
    global resources

    if type(choose) == int:
        check_resources(choose)

    if choose == "back":
        print()
    else:
        if resources == 1:
            if choose == 1:
                water = water - 250
                coffee_beans = coffee_beans - 16
                money = money + 4
                disposable_cups = disposable_cups - 1
            elif choose == 2:
                water = water - 350
                milk = milk - 75
                coffee_beans = coffee_beans - 20
                money = money + 7
                disposable_cups = disposable_cups - 1
            elif choose == 3:
                water = water - 200
                milk = milk - 100
                coffee_beans = coffee_beans - 12
                money = money + 6
                disposable_cups = disposable_cups - 1

def take():
    global money

    print(f"I gave you ${money}")
    money = 0

def fill():

    global water
    global coffee_beans
    global money
    global milk
    global disposable_cups

    print("Write how many ml of water do you want to add:")
    fwater = int(input())
    water = water + fwater
    print("Write how many ml of milk do you want to add:")
    fmilk = int(input())
    milk = milk + fmilk
    print("Write how many grams of coffee beans do you want to add:")
    fcoffee = int(input())
    coffee_beans = coffee_beans + fcoffee
    print("Write how many disposable cups of coffee do you want to add")
    fcups = int(input())
    disposable_cups = disposable_cups + fcups

def remaining():
    printer()
    print()
    action()

def closex():
    global close
    close = 0

def action():
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        closex()

while close == 1:
    action()