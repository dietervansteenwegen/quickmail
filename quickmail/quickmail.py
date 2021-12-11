from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_QuickMail
import GetConfig


class MainWindow(QtWidgets.QMainWindow, Ui_QuickMail):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._get_config()
        self.btn_parse_cred.released.connect(self._get_config)
        self.btn_send.released.connect(self._send_email)

    def _get_config(self):
        self.credentials = GetConfig.get_config()
        missing = GetConfig.check_missing(self.credentials, ('server', 'pw', 'login', 'recipient'))
        if len(missing) > 0:
            self._credentials_ok = False
            self.btn_send.setEnabled(False)
            for i in [self.lbl_server, self.lbl_user, self.lbl_recipient]:
                i.setText('credentials file not complete')
            self.statusbar.showMessage(f'Credentials missing: {missing}!')
            msgbox = QtWidgets.QMessageBox.critical(
                self,
                'Missing credentials',
                f'Missing credentials: {missing}\nPlease edit the credentials file.',
                buttons=QtWidgets.QMessageBox.Ok)
        else:
            self.statusbar.showMessage('')
            self._credentials_ok = True
            self.btn_send.setEnabled(True)
            self.lbl_server.setText(self.credentials['server'])
            self.lbl_user.setText(self.credentials['login'])
            self.lbl_recipient.setText(self.credentials['recipient'])

    def _send_email(self):
        txt = self.txt_mail.toPlainText()
        if len(txt) < 1:
            msgbox = QtWidgets.QMessageBox.warning(
                self,
                'Empty message',
                'The message box is empty, no message to be sent...',
                buttons=QtWidgets.QMessageBox.Ok)
        else:
            self._handleEmail(txt)
            self.statusbar.showMessage(f'Send email: {txt}')

    def _handleEmail(self, txt):
        print(f'message sent: {txt}')


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()