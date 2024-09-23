## Coffee Shop Program
## Author: Mac Hoang Nhat Minh
## Date created: 09 April 2024
## Date last changed: 18 April 2024

## This programme allows users to order drinks from a variety of menu options, apply membership discounts, and make payments.
## I program it base on my real life job at a coffee shop which encouter lots of problems about accounting

## Init orders
orders = []
## Define drinks
DRINKS = [
    {
        "name": "Caffe Americano",
        "sizes": ["S", "M", "L"],
        "prices": [2.65, 2.95, 3.45],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Caffe Misto",
        "sizes": ["S", "M", "L"],
        "prices": [2.85, 2.95, 3.35],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Dark Roast Coffee",
        "sizes": ["S", "M", "L"],
        "prices": [2.15, 2.25, 2.65],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Cappuccino",
        "sizes": ["S", "M", "L"],
        "prices": [3.05, 3.25, 3.75],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Espresso",
        "sizes": ["S", "M", "L"],
        "prices": [2.45, 2.65, 2.95],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Espresso con panna",
        "sizes": ["S", "M", "L"],
        "prices": [2.55, 2.75, 3.05],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Flat White",
        "sizes": ["S", "M", "L"],
        "prices": [4.15, 4.25, 4.75],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Honey Flat White",
        "sizes": ["S", "M", "L"],
        "prices": [4.85, 4.95, 5.45],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Caffe Latte",
        "sizes": ["S", "M", "L"],
        "prices": [3.35, 3.45, 4.25],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Cinnamon Dolce Latte",
        "sizes": ["S", "M", "L"],
        "prices": [3.25, 3.65, 4.25],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Vanilla Latte",
        "sizes": ["S", "M", "L"],
        "prices": [3.85, 3.95, 4.75],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Apple Crisp Macchiato",
        "sizes": ["S", "M", "L"],
        "prices": [4.75, 4.85, 5.45],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Caramel Macchiato",
        "sizes": ["S", "M", "L"],
        "prices": [4.35, 4.45, 4.95],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    },
    {
        "name": "Espresso Macchiato",
        "sizes": ["S", "M", "L"],
        "prices": [2.55, 2.75, 3.05],
        "coffeeStrengths": ["Weak", "Normal", "Strong"],
        "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
        "flavors": ["Caramel", "Vanilla", "Hazelnut"]
    }
]


## Function to write orders to file
def writeOrdersToFile(filename, orders):
    try:
        with open(filename, 'w') as file:
            file.write(
                "{:<25}|{:<10}|{:<10}|{:<15}|{:<15}|{:<15}|{:<10}\n".format("Drink", "Size", "Quantity", "Milk Type", "Strength", "Flavors", "Sugar"))
            file.write("-" * 103 + "\n")
            for order in orders:
                drinkName = order["name"]
                size = order["size"]
                quantity = order["quantity"]
                milkType = order.get("milkType", "")
                strength = order.get("coffeeStrength", "")
                flavors = order.get("flavor", "No")
                sugar = order.get("sugar", "")
                file.write(
                    "{:<25}|{:<10}|{:<10}|{:<15}|{:<15}|{:<15}|{:<10}\n".format(drinkName, size, quantity, milkType, strength, flavors, sugar))
        print(f"Orders written to '{filename}'.")
    except Exception as e:
        print("Error occurred while writing orders to file:", e)


## Function to read orders from file
def readFile(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error occurred while reading '{filename}': {e}")
        return []


## Display the available drinks and their options.
def displayDrinks():
    print("Drinks available:")
    for i, drink in enumerate(DRINKS, 1):
        print(f"{i}. {drink['name']}")


## Get user input with optional validation against a list of options.
def iGetUserInput(prompt, options=None):
    while True:
        iUserInput = input(prompt).strip().capitalize()
        if iUserInput.isdigit():
            return int(iUserInput)
        elif not options:
            return iUserInput
        elif iUserInput in options:
            return iUserInput
        print("Invalid input. Please try again.")


## Calculate the total price of the ordered drinks.
def calculatePrice(drinkName, size, quantity, hasFlavor):
    for drink in DRINKS:
        if drink["name"] == drinkName and size in drink["sizes"]:
            index = drink["sizes"].index(size)
            price = drink["prices"][index] * quantity
            if hasFlavor:
                price += 0.5 * quantity
            return price
    return None


## Calculate membership points based on the total price.
def calculateMembershipPoints(totalPrice):
    return totalPrice // 10


## Calculate the discount based on the membership points.
def calculateDiscount(totalPrice, plusPoints):
    discount = 0
    if plusPoints >= 3:
        discount = 0.1 * totalPrice
    return discount


## Calculate the final price after applying the discount.
def calculateFinalPrice(totalPrice, discount):
    return totalPrice - discount


## Calculate the average price of drinks available.
def calculateAveragePrice():
    totalPrice = sum([min(drink["prices"]) for drink in DRINKS])
    totalQuantity = sum([len(drink["sizes"]) for drink in DRINKS])
    return totalPrice / totalQuantity


## Handle the ordering process for the customer
def orderDrinks():
    orders = []
    totalPrice = 0

    while True:
        displayDrinks()
        print("Ordering:")
        choice = int(iGetUserInput("Choose your drink (enter the number): "))
        drink = DRINKS[choice - 1]

        size = None
        while size not in drink["sizes"]:
            size = iGetUserInput("Choose the size (S,M,L): ", drink["sizes"])

        quantity = 0
        while quantity <= 0:
            quantity = int(iGetUserInput("Choose quantity (1,2,3,...): "))

        hasFlavor = None
        while hasFlavor not in ["Y", "N"]:
            hasFlavor = iGetUserInput("Do you want a flavor? (Y/N): ", ["Y", "N"])
        hasFlavor = hasFlavor == "Y"

        flavorChoice = None
        if hasFlavor:
            print("Available flavors:")
            for i, flavor in enumerate(drink["flavors"], 1):
                print(f"{i}. {flavor}")
            flavorChoice = iGetUserInput("Choose the flavor (enter the number): ",
                                         [str(i) for i in range(1, len(drink["flavors"]) + 1)])

        totalPrice += calculatePrice(drink["name"], size, quantity, hasFlavor)

        milkTypes = ["Fullcream", "Lite", "Almond", "Soy", "Lactose"]
        milkType = None
        while milkType not in range(1, 6):
            milkType = int(input("Choose milk type (1: Fullcream, 2: Lite, 3: Almond, 4: Soy, 5: Lactose): "))
        milkType = milkTypes[milkType - 1]
        print("Selected milk type:", milkType)

        coffeeStrength = None
        strengthMapping = {"1": "Weak", "2": "Normal", "3": "Strong"}

        while coffeeStrength not in strengthMapping.keys():
            coffeeStrength = input("Choose coffee strength (1: Weak, 2: Normal, 3: Strong): ")
            if coffeeStrength not in strengthMapping.keys():
                print("You can only choose 1, 2, or 3.")
        coffeeStrength = strengthMapping[coffeeStrength]

        sugarAdded = None
        while sugarAdded is None:
            userInput = iGetUserInput("Sugar added?(0,1,2,3,...tsp): ")
            if isinstance(userInput, int):
                sugarAdded = userInput

        order = {"name": drink["name"], "size": size, "quantity": quantity, "hasFlavor": hasFlavor, "milkType": milkType, "coffeeStrength": coffeeStrength, "sugar": sugarAdded}
        if hasFlavor:
            order["flavor"] = drink["flavors"][int(flavorChoice) - 1]

        orders.append(order)

        continueOrder = None
        while continueOrder not in ["Y", "N"]:
            continueOrder = iGetUserInput("Do you want to continue ordering? (Y/N): ", ["Y", "N"])
        if continueOrder == "N":
            break
    ## Display orders before confirmation
    print("\nOrders:")
    printOrdersInfo(orders)
    confirm = iGetUserInput("Would you like to confirm your order? (Y/N): ")
    if confirm.lower() == 'y':
        ## Write orders to file:
        writeOrdersToFile('order.txt', orders)

        for order in orders:
            totalPrice += calculatePrice(order["name"], order["size"], order["quantity"], order["hasFlavor"])

        return totalPrice
    else:
        print("Order canceled. See you next time!")
        return False


## Show order infomations for customer to confirm
def printOrdersInfo(orders):
    print(
        "{:<25}|{:<10}|{:<10}|{:<15}|{:<15}|{:<15}|{:<10}".format("Drink", "Size", "Quantity", "Milk Type", "Strength", "Flavors", "Sugar"))
    print("-" * 103)
    for order in orders:
        drinkName = order["name"]
        size = order["size"]
        quantity = order["quantity"]
        milkType = order.get("milkType", "")
        strength = order.get("coffeeStrength", "")
        flavors = order.get("flavor", "No")
        sugar = order.get("sugar", "0")
        print("{:<25}|{:<10}|{:<10}|{:<15}|{:<15}|{:<15}|{:<10}".format(drinkName, size, quantity, milkType, strength, flavors, sugar))
    print()


## Function to verify membership number
def verifyMembershipNumber(memberNumber):
    validMembershipNumbers = [3883, 7375, 8655, 2005, 7377, 4615]
    if memberNumber in validMembershipNumbers:
        return True
    else:
        return False


## Define membership tiers and corresponding discounts
MembershipTiers = {
    3883: "Gold",  ## Gold tier with 10% discount
    7375: "Silver",  ## Silver tier with 6% discount
    8655: "Bronze",  ## Bronze tier with 2% discount
    2005: "Bronze",  ## Bronze tier with 2% discount
    7377: "Silver",  ## Silver tier with 6% discount
    4615: "Bronze",  ## Bronze tier with 2% discount
}

## Define discount percentages for each tier
discountPercentages = {
    "Gold": 0.10,  ## 10% discount
    "Silver": 0.06,  ## 6% discount
    "Bronze": 0.02  ## 2% discount
}


## Verify membership and apply discount if applicable.
def verifyMembership(totalprice):
    membership = iGetUserInput("Do you have a membership? (Y/N): ")
    if membership.lower() == 'y':
        memberNumber = int(iGetUserInput("Please enter your membership number: "))
        if memberNumber in MembershipTiers:
            tier = MembershipTiers[memberNumber]
            print("Membership verified.")
            print(f"Membership number: {memberNumber}")
            print(f"Membership tier: {tier}")
            plusPoints = calculateMembershipPoints(totalprice)
            discountPercentage = discountPercentages[tier]
            discount = discountPercentage * totalprice
            finalPrice = calculateFinalPrice(totalprice, discount)
            print(f"Total price: ${totalprice:.2f}")
            print(f"Plus points earned: {plusPoints}")
            print(f"Discount ({tier} tier): {discountPercentage * 100}%")
            print(f"Final price after discount: ${finalPrice:.2f}")
            return finalPrice
        else:
            print("Invalid membership number. No discount will be applied.")
            return totalprice
    else:
        print("No membership. No discount will be applied.")
        return totalprice


## Process payment for the order.
def payment(finalPrice):
    print(f"Payment: Amount to pay: ${finalPrice:.2f}")
    print("Card only")
    icardNumber = int(input("Enter your card number:"))
    print("Please get your receipt")
    print("Thank you. See you again.")


## Main function to direct the program flow.
def main():
    global orders
    print("Welcome to our shop!")
    while True:
        print("\nOptions:")
        print("1. Show Menu")
        print("2. Order")
        print("3. View previous orders")
        print("4. Exit - close program")

        option = input("Enter your choice: ")

        if option == "1":
            displayDrinks()
        elif option == "2":
            totalPrice = orderDrinks()
            if totalPrice > 0:
                finalPrice = verifyMembership(totalPrice)
                averagePrice = calculateAveragePrice()
                print(f"Average price of drinks: ${averagePrice:.2f}")
                payment(finalPrice)
        elif option == "3":
            filename = 'order.txt'
            lines = readFile(filename)
            if lines:
                for line in lines:
                    print(line.strip())

        elif option == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
