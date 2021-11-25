from PyQt5 import QtCore, QtGui, QtWidgets, uic
from MainWindow import Ui_QuickMail
import GetCredentials


class MainWindow(QtWidgets.QMainWindow, Ui_QuickMail):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._getConfig()
        self.setupWindow()
        self.btn_parse_cred.released.connect(self._getConfig)
        self.btn_send.released.connect(self._sendEmail)

    def _getConfig(self):
        self.credentials = GetCredentials.getCredentials()
        missing = GetCredentials.checkMissing(self.credentials,
                                              ('server', 'pw', 'login', 'recipient'))
        if len(missing) > 0:
            self._credentials_ok = False
            self.btn_send.setEnabled(False)
            for i in [self.lbl_server, self.lbl_user, self.lbl_recipient]:
                i.setText('credentials file not complete')
            msgbox = QtWidgets.QMessageBox.critical(
                self,
                'Missing credentials',
                f'Missing credentials: {missing}\nPlease edit the credentials file.',
                buttons=QtWidgets.QMessageBox.Ok)
        else:
            self._credentials_ok = True
            self.btn_send.setEnabled(True)
            self.lbl_server.setText(self.credentials['server'])
            self.lbl_user.setText(self.credentials['login'])
            self.lbl_recipient.setText(self.credentials['recipient'])

    def _sendEmail(self):
        txt = self.txt_mail.toPlainText()
        if len(txt) < 1:
            msgbox = QtWidgets.QMessageBox.warning(
                self,
                'Empty message',
                'The message box is empty, no message to be sent...',
                buttons=QtWidgets.QMessageBox.Ok)
        else:
            pass
            # self.send()


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()