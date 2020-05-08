# filename: dialog.py

"""Dialog-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle('Dialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

"""
    Line 14 creates a full class Dialog for the GUI, which inherits from QDialog.
    Line 20 assigns a QVBoxLayout object to dlgLaout.
    Line 21 assigns a QVFormLayout object to formLayout.
    Line 22 to 25 add widgets to formLayout.
    Line 26 uses dlgLayout to arrange all the widgets on the form.
    Line 27 provides a convenient object to place the dialog buttons.
    Lines 28 and 29 add two standard buttons: Ok and Cancel.
    Lines 33 to 37 wrap the boilerplate code in an if __name__ == '__main__': idiom. This is considered a best practice for Pythonistas.
"""