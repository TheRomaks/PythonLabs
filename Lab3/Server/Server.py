from  fastapi import FastAPI
from PG import DB
from Recipe import RecipeReq,Recipe
from main import RecipeGenerator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "message"}

@app.post("/recipes_data")
async def get_all_recipes():
    db = DB("localhost", 5430, "recipes_data", "postgres", "password")
    conn = db.connect()
    query = "SELECT * FROM recipes;"
    res=db.execute_query(conn, query)
    return [{"type": row[0],
             "name": row[1],
             "ingredients": row[2],
             "instructions": row[3],} for row in res]

@app.post("/generate_data")
async def generate_recipe():
    recipe_generator = RecipeGenerator("localhost", 5430, "recipes_data", "postgres", "password")
    res=recipe_generator.generate_recipe()
    return res


@app.post("/insert_data")
async def insert_data(data:RecipeReq):
    recipe_generator = RecipeGenerator("localhost", 5430, "recipes_data", "postgres", "password")
    recipe=Recipe(data.type,data.name,data.ingredients,data.instructions)
    recipe_generator.add_recipe(recipe)