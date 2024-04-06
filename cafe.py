#Create a List which will serve as a Menu
Menu = ["Pancake", "Burger", "Apple Crumble", "Salmon"]

#Create a dictionary called stock, the dictionary will contain a Key (Name of Stock) and Value (Costs of the Stock)
Stock = {"Pancake" : 10, "Burger" : 7, "Apple Crumble": 50, "Salmon" : 20}

#Create a dictionary called Prices on your meny and, which should contain prices for each item in your menu.
Price = {"Pancake" : 8.99, "Burger" : 10.99, "Apple Crumble" : 14.99, "Salmon" : 5.00}

#Calculate the Total Stock in the Cafe

Total_Potential_Revenue = 0 #This will act as my container for the result of each loop. 

for Menu_Item in Menu: #This loop will run for each element within the 'Menu' list.
    Potential_Revenue = Stock[Menu_Item] * Price[Menu_Item] #Carrying out the equation.
    Total_Potential_Revenue += Potential_Revenue #Increase the Total Potential Revenue by the outcome of each loop.

print(f"The Total Stock Value for the menu is: £ {Total_Potential_Revenue}")