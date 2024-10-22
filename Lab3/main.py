import sys
import random
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QLineEdit, QTextEdit, QPushButton, QLabel, QDialogButtonBox, QDialog

from PG.db import DB
from errors.db_error import DBError
from Recipe.Recipe import Recipe
from errors.recipe_error import InvalidIngredientError
#from Recipe.Recipe_generator import RecipeGenerator

logging.basicConfig(filename='app.log', level=logging.INFO)

class RecipeGenerator:
    def __init__(self):
        self.db = DB()
        self.recipes = self.load_recipes_from_db()


    def load_recipes_from_db(self):
        conn = self.db.connect()
        if not conn:
            return []

        query = "SELECT type, name, ingredients, instructions FROM Recipes"
        try:
            recipes_data =self.db.execute_query(conn,query)
            recipes = []
            for recipe_data in recipes_data:
                type,name, ingredients, instructions = recipe_data
                ingredients = ingredients.split(',')
                recipes.append(Recipe(type,name, ingredients, instructions))
            self.db.close_connection(conn)
            return recipes
        except DBError as e:
            print(f"Error loading recipes: {str(e)}")
            self.db.close_connection(conn)
            return []

    def generate_recipe(self):
        return random.choice(self.recipes)

    def add_recipe(self,recipe):
        conn = self.db.connect()
        if not conn:
            return []
        self.db.insert_data(conn,recipe.type,recipe.name,recipe.ingredients,recipe.instructions)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.log_field = QTextEdit()
        self.log_field.setReadOnly(True)
        self.initUI()
        self.recipe_generator = RecipeGenerator()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(['Type', 'Recipe Name', 'Ingredients', 'Instructions'])
        layout.addWidget(self.table)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        layout.addWidget(self.log_field)

        label = QLabel("Enter ingredients or generate a random recipe:")
        layout.addWidget(label)
        generate_button = QPushButton("Generate Random Recipe")
        generate_button.clicked.connect(self.generate_recipe)
        layout.addWidget(generate_button)
        add_button = QPushButton("Add New Recipe")
        add_button.clicked.connect(self.add_new_recipe_dialog)
        layout.addWidget(add_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def generate_recipe(self):
        try:
            recipe = self.recipe_generator.generate_recipe()
            self.log_activity(f"Generated Recipe: {recipe.name}")
            logging.info("Generated Recipe")
            self.display_recipe(recipe)
        except Exception as e:
            self.log_activity(f"Error: {str(e)}")
            logging.info("Generate Recipe error")

    def add_new_recipe_dialog(self):
        def submit_recipe():
            try:
                type = type_input.text()
                name = name_input.text()
                ingredients = ingredients_text.toPlainText()
                instructions = instructions_text.toPlainText()

                if not all([type, name, ingredients, instructions]):
                    raise ValueError("Please fill in all fields.")

                recipe = Recipe(type, name, ingredients, instructions)
                self.log_activity(f"Added New Recipe: {recipe.name}")
                self.recipe_generator.add_recipe(recipe)
                self.display_recipe(recipe)
                new_recipe_window.accept()  # Use accept() instead of exec_()

            except InvalidIngredientError as e:
                self.log_activity(f"Error: {str(e)}")
                new_recipe_window.reject()

        new_recipe_window = QDialog(self)
        new_recipe_window.setWindowTitle("Add New Recipe")
        dialog_layout = QVBoxLayout()

        type_label = QLabel("Type:")
        type_input = QLineEdit()
        dialog_layout.addWidget(type_label)
        dialog_layout.addWidget(type_input)

        name_label = QLabel("Name:")
        name_input = QLineEdit()
        dialog_layout.addWidget(name_label)
        dialog_layout.addWidget(name_input)

        ingredients_label = QLabel("Ingredients:")
        ingredients_text = QTextEdit()
        dialog_layout.addWidget(ingredients_label)
        dialog_layout.addWidget(ingredients_text)

        instructions_label = QLabel("Instructions:")
        instructions_text = QTextEdit()
        dialog_layout.addWidget(instructions_label)
        dialog_layout.addWidget(instructions_text)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(submit_recipe)
        button_box.rejected.connect(new_recipe_window.reject)
        dialog_layout.addWidget(button_box)

        new_recipe_window.setLayout(dialog_layout)
        new_recipe_window.exec()  # Use exec() instead of exec_()

    def add_new_recipe_from_dialog(self, type_input, name_input, ingredients_input, instructions_input, dialog):
        try:
            type = type_input.text()
            name = name_input.text()
            ingredients = ingredients_input.toPlainText()
            instructions = instructions_input.toPlainText()

            if not all([type, name, ingredients, instructions]):
                raise ValueError("Please fill in all fields.")

            recipe = Recipe(type, name, ingredients, instructions)
            self.log_activity(f"Added New Recipe: {recipe.name}")
            logging.info("Added New Recipe")
            self.recipe_generator.add_recipe(recipe)
            self.display_recipe(recipe)
            dialog.accept()

        except InvalidIngredientError as e:
            self.log_activity(f"Error: {str(e)}")
            logging.info("Failed to add recipe")
            dialog.reject()

    def log_activity(self, message):
        self.log_field.append(message)

    def display_recipe(self, recipe):
        logging.info("Displayed recipe")
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        self.table.setItem(row, 0, QTableWidgetItem(recipe.type))
        self.table.setItem(row, 1, QTableWidgetItem(recipe.name))
        self.table.setItem(row, 2, QTableWidgetItem(", ".join(recipe.ingredients)))
        self.table.setItem(row, 3, QTableWidgetItem(recipe.instructions))

def main():
    app = QApplication(sys.argv)
    logging.info("Program started")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
