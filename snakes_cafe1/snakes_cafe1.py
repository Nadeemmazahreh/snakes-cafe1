msg = """ 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
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
***********************************"""

print(msg)
total_items =[]


while True:
    order = input(">")
    total_items.append(order)
    order_count = 0
    for i in total_items:
        if (i == order):
            order_count += 1
    
    
    print('** ' + str(order_count) + ' order of ' + str(order) +  ' have been added to your meal **')

    