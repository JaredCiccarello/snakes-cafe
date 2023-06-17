def menu():
    # Tabbing matters: it needs you to be inside of the function
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
  In order to end service, type quit
  When you're done order type 
  Add your new order here>
  """
    print(menu)
    # print menu will print the entire menu.

    menu_items = [
        "wings", "cookies", "spring rolls", "salmon", "steak", "meat tornado",
        "a literal garden", "ice cream", "cake", "pie", "coffee", "tea",
        "unicorn tears"
    ]

    # We want customers to be able to add in orders.
    # First we will need an empty array/list. Remmeber all arrays are now considered lists inside python.

    orders = []



    # Next we set a while loop that sets a true statement. While customer inputs an order, add input.
    while True:
        newOrder = input().lower()
        # As soon as we get the order we need to add this to our "orders" list.
        print(", ".join(orders))
        orders.append(newOrder)

      # While loop needs a way to be stopped. If customer says "quit" the code will break the while loop
      # We also want to tell the user how to quit.
        if newOrder == "quit":
            print ("thank you for using Snakes Cafe!")
            break
        if newOrder == "done":
            print(f"Here's your final order, thank you for using Snakes Cafe!")
            print(f'Final order: {orders}')
            break
      # Next we need to add the new orders to our list. In order to do this we use append to add order to our array
      # If we have menu/orders, we need to append/add the newOrder to our menu.
      # Append cannot be in the same line as an If statement
        if newOrder in orders:
            print(f"** {newOrder} has been added to your order **")
        else:
            print("Sorry, item not in menu")

        if len(orders) > 0:
            print('Please make another selection, if complete type done')
            print('If you would like to start over, type quit')
        else:
            print(
                f"Here's your final order {newOrder}, thank you for using Snakes Cafe!")
            break
        
        def finalOrder():
          while quit == "done":
            break
          

menu()
# if __name__ == "__main__":

# Pay close attention to file structure when running your python3 test. In this case "python3 snakes_cafe.py".
# Careful with your naming, in this case we named both our repo and our folder snakes-cafe. If we are outside of our folder then we will need to use
# "python3 snakes-cafe/snakes_cafe.py"


# Stretch goals:
# Add items only listed in the menu
# Remove "done" in final list
# Allow user to see orders being in display
