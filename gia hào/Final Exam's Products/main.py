from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic
from taikhoan import taikhoan, create_user  # Import the create_user function
import re

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/loginscreen.ui', self)

        self.login_button.clicked.connect(self.loginFn)
        self.signup_button.clicked.connect(self.showSignUp)

    def loginFn(self):
        username = self.username_txt.text()
        password = self.password_txt.text()
                 # Kiểm tra email và mật khẩu có được nhập hay không
        if not username: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        # Kiểm tra email và mật khẩu có khớp với tài khoản admin hay không
        user = taikhoan(username, password, "username")
        if user.login(username, password):
            # Nếu đăng nhập thành công, chuyển sang giao diện chính (Main)
            self.close()
            mainWindow.show()  
        else:
            # Nếu đăng nhập không thành công, hiển thị thông báo lỗi
            msg_box.setText("Username hoặc mật khẩu không đúng!")
            msg_box.exec()
    def showSignUp(self):
        self.close()
        signUpWindow.show()

# Đăng Kí tài khoản 
class SignUp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/signupscreen.ui', self)

        # slot các sự kiện
        self.signup_button.clicked.connect(self.signUpFn)
        self.login_button.clicked.connect(self.showLogin)
    def showLogin(self):
        self.close()
        loginWindow.show()
    def signUpFn(self):
        username = self.username_txt.text()
        email = self.email_txt.text()
        password = self.password_txt.text()
        confirm_password = self.cpwd_txt.text()

        if not username or not email or not password or not confirm_password:
            msg_box.setText("Vui lòng nhập đầy đủ thông tin!")
            msg_box.exec()
            return

        if password != confirm_password:
            msg_box.setText("Mật khẩu không khớp!")
            msg_box.exec()
            return

        if create_user(username, password, email, confirm_password):
            msg_box.setText("Đăng ký thành công!")
            msg_box.exec()
            self.close()
            loginWindow.show()
        else:
            msg_box.setText("Đăng ký thất bại!")
            msg_box.exec()



class FriendList(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/friendlist.ui', self)

class Setting(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/accountsettings.ui', self)

class Profile(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/profile.ui', self)

        self.friendBtn.clicked.connect(self.showFriendList)
    
    def showFriendList(self):
        self.close()
        friendListWindow.exec()  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/homescreen.ui', self)

        self.friendLstBtn.clicked.connect(self.showFriendList)
        self.profileBtn.clicked.connect(self.showProfile)
        self.settingBtn.clicked.connect(self.showSettings)


    def showFriendList(self):
        self.close()
        friendListWindow.exec()  
    def showProfile(self):
        self.close()
        profileWindow.exec()

        # self.friendBtn.clicked.connect(self.showFriendList)  
    def showSettings(self):
        self.close()
        settingsWindow.exec()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = Login()
    signUpWindow = SignUp()
    mainWindow = MainWindow()
    friendListWindow = FriendList()
    profileWindow = Profile()
    settingsWindow = Setting()

    # Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #ffffff; color: #000000")


    loginWindow.show()
    app.exec()