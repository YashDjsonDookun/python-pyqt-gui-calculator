#!/usr/bin/env python3

# Filename: calc.py

"""Just My First Fully Functional GUI using Python and PyQt5"""

import sys

# Import QApplication and the required widgets from PyQt5.QWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from functools import partial


# create a subclass of QMainWindow to setup the calculator's GUI
class CalcUI(QMainWindow):
    """Calc's View GUI"""

    def __init__(self):
        """View Initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("Calculator")
        self.setFixedSize(235, 235)
        # Set the Central Widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the Display"""
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create Buttons"""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the grid layout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text"""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

# Create a Controller class to connect to the GUI and the Model
class CalcCtrl:
    """Calc controller class"""
    def __int__(self, view):
        """Controller Initializer"""
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        """Build expression"""
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
       """Connect signals and slots"""
       for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

       self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

# Client Code
def main():
    """Main Function"""
    # Create an instance of QApplcations
    calc = QApplication(sys.argv)
    # Show the Calculator's GUI
    view = CalcUI()
    view.show()
    # Create instances of the model and the controller
    CalcCtrl(view=view)
    # Execute the calculator's main loop
    sys.exit(calc.exec())


if __name__ == "__main__":
    main()
