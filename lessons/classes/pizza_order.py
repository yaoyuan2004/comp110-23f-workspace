from lessons.classes.pizza import pizza

my_pizza: pizza = ()
my_pizza.size = "large"
my_pizza.toppings = 12
my_pizza.gluten_free = True

sales_pizza: pizza = pizza("medium", 5, False)

def price(a_pizza: pizza) -> float:
    if a_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += 0.75 * a_pizza.toppings
    if a_pizza.gluten_free is True:
        cost += 1.00
    return cost