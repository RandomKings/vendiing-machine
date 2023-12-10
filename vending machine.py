items = {
    "Coca Kala": 450,
    "Bepsi": 350,
    "Fonta": 650,
    "Sprit": 550
}

inputs = ["Coca Kala", "Bepsi", "Fonta", "Sprit"]

def menu():
    print("0: Coca Kala  ($4.50)")
    print("1: Bepsi      ($3.50)")
    print("2: Fonta      ($6.50)")
    print("3: Sprit      ($5.50)")
    print("[X] to exit")

def vendingMachine():
    vending_machine = """
     _________________________
    |  ___   ___   ___   ___  |
    |                         |
    |     Vending Machine     |
    |                         |
    | | 1 | | 2 | | 3 | | 4 | |
    | |___| |___| |___| |___| |
    |_________________________|
    """
    print(vending_machine)
    menu()

bills = input("Input money separated by decimal point: (00.00): ").split(".")
dollars = int(bills[0])
cents = int(bills[1])

coins = dollars * 100 + cents
print(coins)

def convertCoins(coins):
    quarters = coins // 25
    coins %= 25
    dimes = coins // 10
    coins %= 10
    nickels = coins // 5
    pennies = coins % 5
    return quarters, dimes, nickels, pennies

vendingMachine()

def checkIfEnough(coins):
    answer = input("INSUFFICIENT FUNDS.\nWould you like to add more money(Y/N): ").upper()
    if answer == "Y":
        print(f"Current funds: {coins/100}")
        addMoney = float(input("how much more would you like to add: "))
        try:
            coins += addMoney * 100
            print(f"Current Funds: {coins / 100}")
        except ValueError:
            print("PLS INPUT A VALUE")
        return coins
    elif answer == "N":
        quarters, dimes, nickels, pennies = convertCoins(coins)
        print(f"Here are your coins:\n Quarters: {quarters}\n Dimes: {dimes}\n Nickels: {nickels}\n Pennies: {pennies}\n")
        exit(0)
    else:
        print("invalid input")

while True:
    option = input("Choose an option: ")
    if str.upper(option) == "X":
        quarters, dimes, nickels, pennies = convertCoins(coins)
        print(f"Here are your coins:\n Quarters: {quarters}\n Dimes: {dimes}\n Nickels: {nickels}\n Pennies: {pennies}\n")
        print(f"Goodbye, Thank You. Remaining funds: {coins / 100}")
        exit(0)
    option = int(option)
    try:
        if coins < items.get(inputs[option], 0):
            coins = checkIfEnough(coins)
        else:
            coins -= items.get(inputs[option], 0)
            quarters, dimes, nickels, pennies = convertCoins(coins)
            print(
                f"Here are your coins:\n Quarters: {quarters}\n Dimes: {dimes}\n Nickels: {nickels}\n Pennies: {pennies}\n Current funds: {coins / 100}\n")
    except IndexError:
        print("Item does not exist")
