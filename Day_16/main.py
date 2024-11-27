from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("aquamarine")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.setup(width=400, height=300)  # Set up the screen size
#
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
pokemon_names = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff"]
pokemon_types = ["Electric", "Fire/Flying", "Grass/Poison", "Water", "Normal/Fairy"]
table.add_column("Pokemon Name",pokemon_names)
table.add_column("Pokemon types",pokemon_types)
table.align="l"
print(table)
