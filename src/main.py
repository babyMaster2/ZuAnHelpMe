import sys
from PyQt5.QtWidgets import QApplication
from quote_sender.sent_quotes import MyMainWin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_main_win = MyMainWin()
    sys.exit(app.exec_())