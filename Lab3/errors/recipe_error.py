
class RecipeError(Exception):
    pass

class InvalidIngredientError(RecipeError):
    def __init__(self, message):
        super().__init__(message)

