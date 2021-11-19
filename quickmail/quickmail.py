from PyQt5 import QtCore, QtGui, QtWidgets, uic
from MainWindow import Ui_QuickMail
import GetCredentials


class MainWindow(QtWidgets.QMainWindow, Ui_QuickMail):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.getConfig()
        self.setupWindow()
        self.btn_parse_cred.released.connect(self.getConfig)
        self.btn_send.released.connect(self.sendEmail)

    def getConfig(self):
        self.credentials = GetCredentials.getCredentials()
        missing = GetCredentials.checkMissing(self.credentials, ('server', 'pw', 'login'))
        if len(missing) > 0:
            self.label_1.setVisible(True)
            self.label_1.setText(f'Missing credentials: {missing}')
            self.credentials_ok = False
            self.btn_send.setEnabled(False)
        else:
            self.label_1.setVisible(False)
            self.credentials_ok = True
            self.btn_send.setEnabled(True)

    def setupWindow(self):
        pass

    def sendEmail(self):
        txt = self.txt_mail.toPlainText()
        if txt == '':
            self.label_2.setText('No text input')
        else:
            self.label_2.setText(txt)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()