import tkinter as tk
from tkinter import ttk

## Define drinks
DRINKS = [{
    "name": "Caffe Americano",
    "sizes": ["S", "M", "L"],
    "prices": [2.65, 2.95, 3.45],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Caffe Misto",
    "sizes": ["S", "M", "L"],
    "prices": [2.85, 2.95, 3.35],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Dark Roast Coffee",
    "sizes": ["S", "M", "L"],
    "prices": [2.15, 2.25, 2.65],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Cappuccino",
    "sizes": ["S", "M", "L"],
    "prices": [3.05, 3.25, 3.75],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Espresso",
    "sizes": ["S", "M", "L"],
    "prices": [2.45, 2.65, 2.95],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Espresso con panna",
    "sizes": ["S", "M", "L"],
    "prices": [2.55, 2.75, 3.05],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Flat White",
    "sizes": ["S", "M", "L"],
    "prices": [4.15, 4.25, 4.75],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Honey Flat White",
    "sizes": ["S", "M", "L"],
    "prices": [4.85, 4.95, 5.45],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Caffe Latte",
    "sizes": ["S", "M", "L"],
    "prices": [3.35, 3.45, 4.25],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Cinnamon Dolce Latte",
    "sizes": ["S", "M", "L"],
    "prices": [3.25, 3.65, 4.25],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Vanilla Latte",
    "sizes": ["S", "M", "L"],
    "prices": [3.85, 3.95, 4.75],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Apple Crisp Macchiato",
    "sizes": ["S", "M", "L"],
    "prices": [4.75, 4.85, 5.45],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Caramel Macchiato",
    "sizes": ["S", "M", "L"],
    "prices": [4.35, 4.45, 4.95],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}, {
    "name": "Espresso Macchiato",
    "sizes": ["S", "M", "L"],
    "prices": [2.55, 2.75, 3.05],
    "coffeeStrengths": ["Weak", "Normal", "Strong"],
    "milkTypes": ["Fullcream", "Lite", "Almond", "Soy", "Lactose"],
    "flavors": ["Caramel", "Vanilla", "Hazelnut"]
}]


## Show menu to the custumers
def showMenu():
  windowMenu = tk.Toplevel()
  windowMenu.title("Menu")

  lblMenuTitle = tk.Label(windowMenu,
                          text="Menu",
                          font=("Helvetica", 20, "bold"),
                          pady=20)
  lblMenuTitle.pack()

  menuFrame = ttk.Frame(windowMenu)
  menuFrame.pack(fill="both", expand=True)

  menuTree = ttk.Treeview(menuFrame, columns=("Prices"))
  menuTree.heading("#0", text="Drink")
  menuTree.heading("Prices", text="Prices (Large, Medium, Small)")

  for drink in DRINKS:
    priceText = ", ".join([
        f"{size}: ${price:.2f}"
        for size, price in zip(drink['sizes'], drink['prices'])
    ])
    menuTree.insert("", "end", text=drink['name'], values=(priceText, ))

  menuTree.pack(pady=(0, 10), padx=10, fill="both", expand=True)

  btnClose = tk.Button(windowMenu, text="Close", command=windowMenu.destroy)
  btnClose.pack(pady=10)

  windowMenu.mainloop()


## Show previous orders
def viewOrders():
  try:
    with open("order.txt", "r") as file:
      next(file)
      next(file)

      orders = []
      for line in file:
        orderData = line.strip().split('|')
        orders.append(orderData)

      if orders:
        windowOrders = tk.Toplevel()
        windowOrders.title("Previous Orders")

        tree = ttk.Treeview(windowOrders,
                            columns=("Drink", "Size", "Quantity", "Price",
                                     "Coffee Strength", "Flavor", "Milk Type",
                                     "Sugar"),
                            show="headings",
                            height=20)
        tree.heading("Drink", text="Drink")
        tree.heading("Size", text="Size")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")
        tree.heading("Coffee Strength", text="Coffee Strength")
        tree.heading("Flavor", text="Flavor")
        tree.heading("Milk Type", text="Milk Type")
        tree.heading("Sugar", text="Sugar")

        for order in orders:
          tree.insert("", "end", values=order)

        tree.pack(fill="both", expand=True, padx=10, pady=10)
      else:
        tk.messagebox.showinfo("Previous Orders", "No previous orders found.")
  except FileNotFoundError:
    tk.messagebox.showinfo("Previous Orders", "No previous orders found.")


## Handle the ordering process for the customer
def orderDrinks():


  def addToOrder():
    if not drinksListbox.curselection():
      print("Please select a drink.")
      return

    selectedDrinkIndex = drinksListbox.curselection()[0]
    selectedDrink = DRINKS[selectedDrinkIndex]
    size = sizeDrink.get()
    quantityItem = quantity.get()
    strengthItem = coffeeStrength.get()
    myFlavor = flavor.get()
    milkTypes = milkType.get()
    sugarAmount = sugar.get()
    theMembership = membership.get()
    taxRate = tax.get() / 100

    try:
      pricePerUnit = selectedDrink["prices"][selectedDrink["sizes"].index(
          size)]
    except ValueError:
      print("Invalid size selected.")
      return

    ## Flavor price adjustment
    flavorPrice = 0
    if myFlavor != "None":
      flavorPrice = 0.5

    price = (pricePerUnit + flavorPrice) * quantityItem

    ## Apply membership discount if applicable
    if theMembership == "Bronze":
      price *= 0.97
    elif theMembership == "Silver":
      price *= 0.94
    elif theMembership == "Gold":
      price *= 0.90

    priceWithDiscount = price * (1 + taxRate)

    trvOrder.insert("",
                    "end",
                    text=selectedDrink["name"],
                    values=(size, quantityItem, f"${priceWithDiscount:.2f}",
                            strengthItem, myFlavor, milkTypes, sugarAmount,
                            theMembership))

    totalPrice = sum(
        float(trvOrder.item(item, "values")[2][1:])
        for item in trvOrder.get_children())
    lblTotalPrice.config(text=f"Total Price: ${totalPrice:.2f}")

    ## Reset all options to default
    sizeDrink.set("S")
    quantity.set(1)
    coffeeStrength.set("Normal")
    flavor.set("None")
    milkType.set("Fullcream")
    sugar.set(0)
    membership.set("None")
    tax.set(8)


  def saveOrder():
    try:
      with open("order.txt", "w") as file:
        file.write(
            "{:<25} | {:<10} | {:<10} | {:<10} | {:<15} | {:<15} | {:<10} | {:<10}\n"
            .format("Name", "Size", "Quantity", "Price", "Coffee Strength",
                    "Flavor", "Milk Type", "Sugar"))
        file.write("-" * 125 + "\n")
        for item in trvOrder.get_children():
          itemText = trvOrder.item(item, "text")
          itemValues = trvOrder.item(item, "values")
          name = itemText
          size = itemValues[0]
          quantity = itemValues[1]
          price = itemValues[2]
          strengthItem = itemValues[3]
          flavor = itemValues[4]
          milkType = itemValues[5]
          sugar = itemValues[6]
          file.write(
              "{:<25} | {:<10} | {:<10} | {:<10} | {:<15} | {:<15} | {:<10} | {:<10}\n"
              .format(name, size, quantity, price, strengthItem, flavor,
                      milkType, sugar))
      print("Order saved successfully!")
    except Exception as e:
      print("Error occurred while saving order:", e)

  windowOrders = tk.Toplevel()
  windowOrders.title("Order Drinks")

  ## Listbox to
  drinksListbox = tk.Listbox(windowOrders, selectmode="single")
  for drink in DRINKS:
    drinksListbox.insert("end", drink["name"])
  drinksListbox.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

  optionsFrame = ttk.LabelFrame(windowOrders, text="Options")
  optionsFrame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

  sizeDrink = tk.StringVar()
  sizeDrink.set("S")
  lblSize = tk.Label(optionsFrame, text="Select size:")
  lblSize.grid(row=0, column=0, padx=10, pady=5, sticky="w")
  optSize = tk.OptionMenu(optionsFrame, sizeDrink, *["S", "M", "L"])
  optSize.grid(row=0, column=1, padx=10, pady=5, sticky="w")

  quantity = tk.IntVar()
  quantity.set(1)
  lblQuantity = tk.Label(optionsFrame, text="Quantity:")
  lblQuantity.grid(row=1, column=0, padx=10, pady=5, sticky="w")
  entQuantity = tk.Entry(optionsFrame, textvariable=quantity)
  entQuantity.grid(row=1, column=1, padx=10, pady=5, sticky="w")

  coffeeStrength = tk.StringVar()
  coffeeStrength.set("Normal")
  lblCoffeeStrength = tk.Label(optionsFrame, text="Select coffee strength:")
  lblCoffeeStrength.grid(row=2, column=0, padx=10, pady=5, sticky="w")
  optCoffeeStrength = tk.OptionMenu(optionsFrame, coffeeStrength,
                                    *["Weak", "Normal", "Strong"])
  optCoffeeStrength.grid(row=2, column=1, padx=10, pady=5, sticky="w")

  flavor = tk.StringVar()
  flavor.set("None")
  lblFlavor = tk.Label(optionsFrame, text="Select flavor:")
  lblFlavor.grid(row=3, column=0, padx=10, pady=5, sticky="w")
  optFlavor = tk.OptionMenu(optionsFrame, flavor,
                            *["None"] + DRINKS[0]["flavors"])
  optFlavor.grid(row=3, column=1, padx=10, pady=5, sticky="w")

  milkType = tk.StringVar()
  milkType.set("Fullcream")
  lblType = tk.Label(optionsFrame, text="Select Milk Type:")
  lblType.grid(row=4, column=0, padx=10, pady=5, sticky="w")
  optType = tk.OptionMenu(optionsFrame, milkType,
                          *["Fullcream", "Lite", "Almond", "Soy", "Lactose"])
  optType.grid(row=4, column=1, padx=10, pady=5, sticky="w")

  sugar = tk.IntVar()
  sugar.set(0)
  lblSugar = tk.Label(optionsFrame, text="Sugar(0,1,... tsp):")
  lblSugar.grid(row=5, column=0, padx=10, pady=5, sticky="w")
  entSugar = tk.Entry(optionsFrame, textvariable=sugar)
  entSugar.grid(row=5, column=1, padx=10, pady=5, sticky="w")

  membership = tk.StringVar()
  membership.set("None")
  lblMembership = tk.Label(optionsFrame, text="Select membership:")
  lblMembership.grid(row=6, column=0, padx=10, pady=5, sticky="w")
  optMembership = tk.OptionMenu(optionsFrame, membership,
                                *["None", "Bronze", "Silver", "Gold"])
  optMembership.grid(row=6, column=1, padx=10, pady=5, sticky="w")

  tax = tk.DoubleVar()
  tax.set(8)
  lblTax = tk.Label(optionsFrame, text="Tax (in %):")
  lblTax.grid(row=7, column=0, padx=10, pady=5, sticky="w")
  entTax = tk.Entry(optionsFrame, textvariable=tax)
  entTax.grid(row=7, column=1, padx=10, pady=5, sticky="w")

  lblTotalPrice = tk.Label(optionsFrame, text="Total Price: $0.00")
  lblTotalPrice.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

  btnAdd = tk.Button(optionsFrame, text="Order", command=addToOrder)
  btnAdd.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

  ## Treeview to display the order
  trvOrder = ttk.Treeview(windowOrders,
                          columns=("Size", "Quantity", "Price",
                                   "Coffee Strength", "Flavor", "Milk Type",
                                   "Sugar"))
  trvOrder.heading("#0", text="Name", anchor="center")
  trvOrder.heading("Size", text="Size", anchor="center")
  trvOrder.heading("Quantity", text="Quantity", anchor="center")
  trvOrder.heading("Price", text="Price", anchor="center")
  trvOrder.heading("Coffee Strength", text="Coffee Strength", anchor="center")
  trvOrder.heading("Flavor", text="Flavor", anchor="center")
  trvOrder.heading("Milk Type", text="Milk Type", anchor="center")
  trvOrder.heading("Sugar", text="Sugar Amount", anchor="center")
  trvOrder.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

  ## Save button to write in file
  btnSave = tk.Button(optionsFrame, text="Save", command=saveOrder)
  btnSave.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

  windowOrders.rowconfigure(0, weight=1)
  windowOrders.columnconfigure(0, weight=1)


## Main function to direct the program flow.
def main():
  root = tk.Tk()
  root.title("Coffee Shop")

  lblWelcome = tk.Label(root,
                        text="Welcome to My Coffee Shop!",
                        font=("Helvetica", 18, "bold"),
                        pady=20)
  lblWelcome.pack()

  lblContactInfo = tk.Label(root,
                            text="Contact Information:",
                            font=("Helvetica", 12, "bold"))
  lblContactInfo.pack()

  lblAddress = tk.Label(root,
                        text="31 Liffey Circuit, Kaleen, ACT 2617 ",
                        font=("Helvetica", 10))
  lblAddress.pack()

  lblPhone = tk.Label(root, text="Phone: 0491-768-460", font=("Helvetica", 10))
  lblPhone.pack()

  lblEmail = tk.Label(root,
                      text="Email: machoangnhatminh@gmail.com",
                      font=("Helvetica", 10))
  lblEmail.pack()

  btnMenu = tk.Button(root, text="Menu", command=showMenu, font=("Helvetica", 15, "bold"), width=30, height=3, bd=3, background="Green")
  btnMenu.pack(pady=40)

  btnOrder = tk.Button(root, text="Order Drinks", command=orderDrinks, font=("Helvetica", 15, "bold"), width=30, height=3, bd=3, background="Green")
  btnOrder.pack(pady=40)

  btnViewOrders = tk.Button(root,text="View Orders",command=viewOrders, font=("Helvetica", 15, "bold"), width=30, height=3, bd=3, background="Green")
  btnViewOrders.pack(pady=40)

  btnExit = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 15, "bold"), width=30, height=3, bd=3, background="Red")
  btnExit.pack(pady=40)

  root.mainloop()


if __name__ == "__main__":
  main()
