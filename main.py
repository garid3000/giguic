import sys
from PySide2.QtWidgets import QApplication # QtCore
from Custom_Widgets.Lib_Mainwindow import TheMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TheMainWindow()
    # w.setWindowFlags(
    #    QtCore.Qt.WindowType.WindowContextHelpButtonHint | QtCore.Qt.WindowType.WindowCloseButtonHint
    # )
    w.show()
    sys.exit(app.exec_())
