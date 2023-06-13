def menu():
    #Tabbing matters: it needs you to be inside of the function
  menu = """

**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **

** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
--------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
"""

  print(menu)
  #Doing this invokes the menu outside of 




  # We want customers to be able to add in orders.
  # First we will need an empty array

orders = []

  #Next we set a while loop that sets a true statement. While customer inputs an order, add input.
while True: 
      newOrder = input()

    # While loop needs a way to be stopped. If customer says "quit" the code will break the while loop
      if newOrder == "quit":
        break

    # Next we need to add the new orders to our list. In order to do this we use append to add order to our array
    # If we have menu/orders, we need to append/add the newOrder to our menu.
      if orders.append(newOrder):
        print (f"** {newOrder} has been added to your order")
      else: 
       print ("Sorry, item not in menu")

      #Lastly we need to show our customer a list of their order
      for newOrder in orders:
        print(orders)

menu()
# if __name__ == "__main__":