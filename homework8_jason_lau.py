pizza_orders = ["cheese", "vegan", "hawaiian", "mushroom"]
finished_pizzas = []
while pizza_orders: 
    current_pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)
    print("The pizza", current_pizza, "was made.")
