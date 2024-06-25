import sys
from PySide6.QtWidgets import QApplication, QMessageBox # QtCore
from Custom_Widgets.Lib_Mainwindow import TheMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TheMainWindow()
    w.show()
    sys.exit(app.exec_())
