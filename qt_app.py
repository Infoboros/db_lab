import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui.main_form import MainForm

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QWidget()
    ui = MainForm(w)
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())