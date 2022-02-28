# <----- READ ME ----->
# Build a game using the concept of objects and classes. The main algorithm to implement to modify the burger is to use the concept of stacks and its theory of FIFO (stack implementation: https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm). In other words, when adding ingredients to the burger, the ingredients will be added to the end of the list. The main implementation of the game can be found under the `main` function.

class Burger:
    def __init__(self):
        self.burger = []

    # <----- TO DO: finish this function that will take an ingredient as a string to be added t the burger ----->
    def add_ingredients(self, ingredient):
        pass   

    # <----- TO DO: finish this function to print the burger ----->
    # Example burger: ["bun", "lettuce", "mayonnaise", "tomato", "patty", "cheese", "bun"]
    # Example output:
    #  bun
    #  cheese
    #  patty
    #  tomato
    #  mayonnaise
    #  lettuce
    #  bun
    def serve_burger(self):
        pass

def main():
    burger = Burger()
    userInput = True
    while userInput != "q":
        userInput = input("Add your ingredient (q to quit): ")
        burger.add_ingredients(userInput)
    burger.serve_burger()
    return 

if __name__ == "__main__":
    main()
