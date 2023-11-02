class pizza:
    """The pizza attribute setting"""


    size: str
    toppings: int
    gluten_free: bool


    def __init__(self, x: str, y: int, z: bool):
        self.size = x
        self.toppings = y
        self.gluten_free = z


    def price(self) -> float:
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += 0.75 * self .toppings
        if self.gluten_free is True:
            cost += 1.00
        return cost
