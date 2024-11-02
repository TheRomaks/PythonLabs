import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem, QSpinBox, QLabel
import random
from string import ascii_lowercase, ascii_uppercase
from tasks import multiply_lists


class AbsNumbersTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.a_input = QLineEdit()
        self.b_input = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        self.result_text = QTextEdit()

        self.layout.addWidget(QLabel("Enter a:"))
        self.layout.addWidget(self.a_input)
        self.layout.addWidget(QLabel("Enter b:"))
        self.layout.addWidget(self.b_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_text)

        self.calculate_button.clicked.connect(self.calculate_abs_numbers)

    def calculate_abs_numbers(self):
        try:
            a = int(self.a_input.text())
            b = int(self.b_input.text())
            if a >= b:
                raise ValueError("a должно быть меньше b.")
            generator = (abs(num) for num in range(a, b + 1))
            result = list(generator)[:4]
            self.result_text.setPlainText('\n'.join(map(str, result)))
        except ValueError as e:
            self.result_text.setPlainText(f"Ошибка: {e}")

class PasswordsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.length_input = QLineEdit()
        self.generate_button = QPushButton("Generate Passwords")
        self.result_text = QTextEdit()

        self.layout.addWidget(QLabel("Enter password length:"))
        self.layout.addWidget(self.length_input)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.result_text)

        self.generate_button.clicked.connect(self.generate_passwords)

    def generate_passwords(self):
        try:
            length = int(self.length_input.text())
            if length < 1:
                raise ValueError("Такой пароль не может быть")
            chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
            passwords = [''.join(random.choice(chars) for _ in range(length)) for _ in range(5)]
            self.result_text.setPlainText('\n'.join(passwords))
        except ValueError as e:
            self.result_text.setPlainText(f"Ошибка: {e}")

class ListsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.list_size_input = QSpinBox()
        self.list_size_input.setMinimum(3)
        self.generate_lists_button = QPushButton("Generate Lists")
        self.list1_table = QTableWidget()
        self.list2_table = QTableWidget()
        self.create_and_multiply_button = QPushButton("Create and Multiply Lists")
        self.result_text = QTextEdit()

        self.layout.addWidget(QLabel("Enter list size:"))
        self.layout.addWidget(self.list_size_input)
        self.layout.addWidget(self.generate_lists_button)
        self.layout.addWidget(QLabel("List 1:"))
        self.layout.addWidget(self.list1_table)
        self.layout.addWidget(QLabel("List 2:"))
        self.layout.addWidget(self.list2_table)
        self.layout.addWidget(self.create_and_multiply_button)
        self.layout.addWidget(self.result_text)

        self.generate_lists_button.clicked.connect(self.generate_empty_lists)
        self.create_and_multiply_button.clicked.connect(self.create_and_multiply_lists)

    def generate_empty_lists(self):
        list_count = self.list_size_input.value()
        self.list1_table.setRowCount(list_count)
        self.list1_table.setColumnCount(1)
        self.list2_table.setRowCount(list_count)
        self.list2_table.setColumnCount(1)
        for i in range(list_count):
            self.list1_table.setItem(i, 0, QTableWidgetItem())
            self.list2_table.setItem(i, 0, QTableWidgetItem())

    def create_and_multiply_lists(self):
        try:
            list_count = self.list_size_input.value()
            list1 = [int(self.list1_table.item(i, 0).text()) for i in range(list_count)]
            list2 = [int(self.list2_table.item(i, 0).text()) for i in range(list_count)]
            result = multiply_lists(list1,list2)
            self.result_text.setPlainText('\n'.join(map(str, result)))
        except Exception as e:
            self.result_text.setPlainText(f"Ошибка: {e}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.abs_numbers_tab = AbsNumbersTab()
        self.passwords_tab = PasswordsTab()
        self.lists_tab = ListsTab()

        self.tab_widget.addTab(self.abs_numbers_tab, "Absolute Numbers")
        self.tab_widget.addTab(self.passwords_tab, "Generate Passwords")
        self.tab_widget.addTab(self.lists_tab, "Create and Multiply Lists")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())