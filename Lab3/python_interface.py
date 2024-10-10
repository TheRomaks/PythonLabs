import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QTextEdit, QPushButton, QLabel
import pyqtgraph as pg
# чисто прикол затестил
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         central_widget = QWidget()
#         layout = QVBoxLayout()
#
#         # Таблица
#         self.table = QTableWidget(5, 3)
#         self.table.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])
#         layout.addWidget(self.table)
#
#         # Поле ввода
#         self.input_field = QLineEdit()
#         layout.addWidget(self.input_field)
#
#         # График активности
#         self.graph_widget = pg.PlotWidget()
#         layout.addWidget(self.graph_widget)
#
#         # Логирование активности
#         self.log_field = QTextEdit()
#         self.log_field.setReadOnly(True)
#         layout.addWidget(self.log_field)
#
#         # Кнопки и лейблы
#         label = QLabel("Example Label")
#         layout.addWidget(label)
#         button = QPushButton("Click Me")
#         button.clicked.connect(self.button_clicked)
#         layout.addWidget(button)
#
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#     def log_activity(self, message):
#         self.log_field.append(message)
#
#     def button_clicked(self):
#         self.log_activity("Button clicked")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())