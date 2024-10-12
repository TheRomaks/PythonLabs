import random
from Lab3.errors.db_error import DBError
from Recipe import Recipe


class RecipeGenerator:
    def __init__(self):
        self.recipes = self.load_recipes_from_db()

    def load_recipes_from_db(self):
        conn = db.connect()
        if not conn:
            return []

        query = "SELECT name, ingredients, instructions FROM recipes"
        try:
            recipes_data = db.execute_query(conn, query)
            recipes = []
            for recipe_data in recipes_data:
                name, ingredients, instructions = recipe_data
                ingredients = ingredients.split(',')
                recipes.append(Recipe(name, ingredients, instructions))
            db.close_connection(conn)
            return recipes
        except DBError as e:
            print(f"Error loading recipes: {str(e)}")
            db.close_connection(conn)
            return []

    def generate_recipe(self):
        return random.choice(self.recipes)
