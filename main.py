# <----- READ ME ----->
# Build a game using the concept of objects and classes. The main algorithm to implement to modify the burger is to use the concept of stacks and its theory of LIFO (stack implementation: https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm). In other words, when adding ingredients to the burger, the ingredients will be added to the end of the list. The main implementation of the game can be found under the `main` function.

class Burger:
    def __init__(self):
        self.burger = []

    # <----- TO DO: finish this function that will take an ingredient as a string to be added to the burger ----->
    def add_ingredients(self, ingredient):
        pass

    # <----- TO DO: finish this function to print the burger ----->
    # Example burger: ["patty", "cheese", "bun"]
    # Example output:
    # bun
    # cheese
    # patty
    def serve_burger(self):
        pass
    
    # <----- TO DO: finish this function to remove the ingredient at the top of the stack ----->
    # Example burger: ["patty", "cheese", "bun"]
    # Element to be returned: bun
    def pop_ingredient(self):
        pass

def main():
    burger = Burger()
    burger.add_ingredients('bun')
    burger.add_ingredients('lettuce')
    burger.add_ingredients('mayonnaise')
    burger.add_ingredients('tomato')
    burger.add_ingredients('patty')
    burger.add_ingredients('cheese')
    burger.add_ingredients('bun')
    burger.add_ingredients('sesame seed')
    topIngredient = burger.pop_ingredient()
    print("Ingredient on top: " + topIngredient)    
    burger.serve_burger()

if __name__ == "__main__":
    main()
