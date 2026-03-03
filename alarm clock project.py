import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


#Contructing entites for the clock
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

# Layout of digital clock
    def initUI(self):
        pass

if __name__ == "__main__":
    #argv = arguments
    app = QApplication(sys.argv)
    clock = DigitalClock()
    #shows clock but for a second
    clock.show()
    #access module of sys.  does execture methods
    sys.exit(app.exec_())