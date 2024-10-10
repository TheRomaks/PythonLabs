import random
from Recipe import Recipe


class RecipeGenerator:
    def __init__(self):
        self.recipes = [
            Recipe("Spaghetti Bolognese", ["spaghetti", "ground beef", "tomato sauce"], "Cook spaghetti, mix with ground beef and tomato sauce."),
            Recipe("Grilled Chicken", ["chicken breast", "olive oil", "salt", "pepper"], "Grill chicken breast with olive oil, salt, and pepper."),
            # Придумать как это по-человечески сделать
        ]

    def generate_recipe(self):
        return random.choice(self.recipes)
