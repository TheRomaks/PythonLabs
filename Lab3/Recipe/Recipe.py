from pydantic import BaseModel

class RecipeReq(BaseModel):
    type:str
    name:str
    ingredients:str
    instructions:str

class Recipe:
    def __init__(self,type, name, ingredients, instructions):
        self.type=type
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"