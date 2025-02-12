import os, sys, subprocess, time
from ui_pycode.main import Ui_Main
from info import *
from db_connect import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(AppName)
        self.switch_general()
        self.set_username()

        self.btn_general.clicked.connect(self.switch_general)
        self.btn_username.clicked.connect(self.switch_username)
        self.btn_connect.clicked.connect(self.connect)

    def connect_db(self):
        with Session() as session:
            user = session.query(Connection).first()
            try:
                return user
            except Exception as e:
                self.get_error(f"\n{e}")

    def switch_general(self):
        self.stackedWidget.setCurrentIndex(0)
        user = self.connect_db()
        self.input_port.setText(user.port_number)

    def switch_username(self):
        self.stackedWidget.setCurrentIndex(1)
        self.input_username.setFocus()

    def set_username(self):
        self.input_username.clear()

        user = self.connect_db()
        if user.log_username is None:
            username = user.default_username
        else:
            username = user.log_username

        self.input_username.setText(username)

    # Update username
    def UpdateUserAndPort(self):
        username = self.input_username.text().strip().upper()
        port_number = self.input_port.text()

        if username:
            with Session() as session:
                user = session.query(Connection).first()
                if self.checkbox_save_me.isChecked():
                    user.default_username = username

                user.log_username = username
                user.port_number = port_number
                session.commit()
        else:
            self.get_error(f"\nEnter Username!")


    # Control ip and password and connect remote desktop
    def connect(self):
        self.UpdateUserAndPort()

        user = self.connect_db()
        if user.log_username is None:
            username = user.default_username
        else:
            username = user.log_username

        ip_address = self.input_ip_address.text()
        port_number = self.input_port.text()
        password = self.input_password.text()

        if not ip_address:
            self.get_error(f"\nEnter IP address!")
        elif not password:
            self.get_error(f"\nEnter password!")
        else:
            self.input_ip_address.clear()
            self.input_password.clear()
            if port_number:
                complete_address = ip_address+':'+port_number
            else:
                complete_address = ip_address

            self.remote_desktop_connection(ip_address, username, password, complete_address)


    def remote_desktop_connection(self, ip_address, username, password, complete_address):
        # Create the RDP file path
        rdp_file_path = os.path.join(os.environ['HOMEPATH'], 'Documents', 'local.rdp')
        
        # Create the RDP file with local resource settings
        with open(rdp_file_path, 'w') as rdp_file:
            rdp_file.write(f"full address:s:{complete_address}\n")
            rdp_file.write("redirectprinters:i:1\n")  # Enable printer redirection
            rdp_file.write("redirectclipboard:i:1\n")  # Enable clipboard redirection
            rdp_file.write("redirectcomports:i:1\n")  # Enable COM port redirection

        credentials = f'cmdkey /generic:{ip_address} /user:{username} /pass:{password}'
        connect = f'mstsc "{rdp_file_path}"'

        # Commands to clean up after connection
        delete_connection = f'cmdkey /delete:{ip_address}'
        delete_connection_term = f'cmdkey /delete:TERMSRV/{ip_address}'
        delete_TSC = r'reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client" /f'
        delete_hidden_default_rdp = f'del /ah "{os.path.join(os.environ["HOMEPATH"], "Documents", "Default.rdp")}"'
        delete_default_rdp = f'del "{os.path.join(os.environ["HOMEPATH"], "Documents", "Default.rdp")}"'
        delete_default_rdp = f'del "{os.path.join(os.environ["HOMEPATH"], "Documents", "local.rdp")}"'

        # List of commands to execute
        commands = [credentials, connect, delete_connection, delete_connection_term, delete_TSC,
                    delete_hidden_default_rdp, delete_default_rdp]
        
        self.close()

        for command in commands:
            try:
                proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                proc.communicate()
                time.sleep(0.08)
            except Exception as e:
                self.get_error(f"\n{e}")


    # Show Error
    def get_error(self, error):
        QMessageBox.critical(self, AppName, f"{error}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())
