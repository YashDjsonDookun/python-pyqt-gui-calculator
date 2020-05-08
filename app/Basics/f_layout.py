# Filename: f_layout.py

"""Form layout Example"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QForm Layout")
layout = QFormLayout()
layout.addRow('Name:', QLineEdit())
layout.addRow('Age:',QLineEdit())
layout.addRow('Job:',QLineEdit())
layout.addRow('Hobbies:',QLineEdit())
window.setLayout(layout)
window.show()

sys.exit(app.exec_())