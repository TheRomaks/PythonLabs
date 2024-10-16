import random

from Lab3.Database.db import DB
from Lab3.errors.db_error import DBError
from Recipe import Recipe


# class RecipeGenerator:
#     def __init__(self,host:str,port:int,database:str,user:str,password:str):
#         self.db = DB(host, port, database, user, password)
#         self.recipes = self.load_recipes_from_db()
#
#
#     def load_recipes_from_db(self):
#         conn = self.db.connect()
#         if not conn:
#             return []
#
#         query = "SELECT type, name, ingredients, instructions FROM Recipes"
#         try:
#             recipes_data =self.db.execute_query(conn,query)
#             recipes = []
#             for recipe_data in recipes_data:
#                 type,name, ingredients, instructions = recipe_data
#                 ingredients = ingredients.split(',')
#                 recipes.append(Recipe(type,name, ingredients, instructions))
#             self.db.close_connection(conn)
#             return recipes
#         except DBError as e:
#             print(f"Error loading recipes: {str(e)}")
#             self.db.close_connection(conn)
#             return []
#
#     def generate_recipe(self):
#         return random.choice(self.recipes)
#
#     def add_recipe(self,recipe):
#         conn = self.db.connect()
#         if not conn:
#             return []
#         self.db.insert_data(conn,recipe.type,recipe.name,recipe.ingredients,recipe.instructions)
