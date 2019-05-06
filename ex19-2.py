def pizza_and_pepperoni(pizzas, pepperoni):
    print(f"You have {pizzas} pizzas!")
    print(f"You have {pepperoni} pepperoni!")
    pepperoni_with_pizzas = pepperoni / pizzas
    print(f"You have {pepperoni_with_pizzas} peperonis with each pizza!\n")


pizza_and_pepperoni(10,50)


pizzas = 1
pepperoni = 3

pizza_and_pepperoni(pizzas, pepperoni)


pizza_and_pepperoni(2,3)    # thought division reverted to using ints and not floats?