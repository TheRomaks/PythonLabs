import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QLineEdit, QTextEdit, QPushButton, QLabel
from Recipe.Recipe import Recipe
from errors.recipe_error import InvalidIngredientError
from Recipe.Recipe_generator import RecipeGenerator

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.log_field = QTextEdit()
        self.log_field.setReadOnly(True)
        self.initUI()
        self.recipe_generator = RecipeGenerator

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(['Recipe Name', 'Ingredients', 'Instructions'])
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
        add_button.clicked.connect(self.add_new_recipe)
        layout.addWidget(add_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def generate_recipe(self):
        try:
            recipe = self.recipe_generator.generate_recipe()
            self.log_activity(f"Generated Recipe: {recipe.name}")
            self.display_recipe(recipe)
        except Exception as e:
            self.log_activity(f"Error: {str(e)}")

    def add_new_recipe(self):
        try:
            input_field_split=self.input_field.text().split(";")
            name = input_field_split[0]
            if not name:
                raise InvalidIngredientError("Recipe name is required")
            ingredients = input_field_split[1]
            instructions = input_field_split[2]
            recipe = Recipe(name, ingredients, instructions)
            self.log_activity(f"Added New Recipe: {recipe.name}")
            self.display_recipe(recipe)
        except InvalidIngredientError as e:
            self.log_activity(f"Error: {str(e)}")

    def log_activity(self, message):
        self.log_field.append(message)

    def display_recipe(self, recipe):
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        self.table.setItem(row, 0, QTableWidgetItem(recipe.name))
        self.table.setItem(row, 1, QTableWidgetItem(recipe.ingredients))
        self.table.setItem(row, 2, QTableWidgetItem(recipe.instructions))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
