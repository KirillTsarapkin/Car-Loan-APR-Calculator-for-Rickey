from PyQt5 import QtWidgets, uic, QtGui, QtCore
from apr import *
import sys
from PyQt5.QtWidgets import QMessageBox
import re

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #Load the UI Page
        uic.loadUi('apr_calc.ui', self)
        self.setWindowIcon(QtGui.QIcon("icon.ico"))

        self.label_18.setOpenExternalLinks(True)

        # Connect user-inputs to update functions
        self.lineEdit.textChanged.connect(self.inputbox_loan_amount)
        self.lineEdit_2.textChanged.connect(self.inputbox_loan_term)
        self.lineEdit_3.textChanged.connect(self.inputbox_apr)
        self.lineEdit_4.textChanged.connect(self.inputbox_tax)

        # Connect button click inputs from the user.
        self.calc_button = self.findChild(QtWidgets.QPushButton, 'Calc_Button')
        self.calc_button.clicked.connect(LoanCalculator.loan_calc)
        self.calc_button.clicked.connect(self.append_warning_msgs)
        self.calc_button.clicked.connect(self.append_result_msgs)

        self.clear_button = self.findChild(QtWidgets.QPushButton, 'Clear_Button')
        self.clear_button.clicked.connect(self.clear_everything)

        self.sim1_button = self.findChild(QtWidgets.QPushButton, 'sim_1')
        self.sim1_button.clicked.connect(self.simulation_1)
        self.sim2_button = self.findChild(QtWidgets.QPushButton, 'sim_2')
        self.sim2_button.clicked.connect(self.simulation_2)
        self.sim3_button = self.findChild(QtWidgets.QPushButton, 'sim_3')
        self.sim3_button.clicked.connect(self.simulation_3)
        self.sim4_button = self.findChild(QtWidgets.QPushButton, 'sim_4')
        self.sim4_button.clicked.connect(self.simulation_4)

    # Store user-input
    # Note to self, text_input is initially stored as a string.
    def inputbox_loan_amount(self, text_input):
        try:
            UserParameters.amount_borrowed = float(text_input)
            print(f'Loan amount entered: ${str(UserParameters.amount_borrowed)}')
        except:
            # Remove special characters and letters from input and keep only numbers and "."
            try:
                UserParameters.amount_borrowed = float(re.sub("[^.0-9]", "", text_input))
                self.lineEdit.setText(str(UserParameters.amount_borrowed))
            except:
                UserParameters.amount_borrowed = ""
                self.lineEdit.setText("")

    def inputbox_loan_term(self, text_input):
        try:
            UserParameters.number_of_months = float(text_input)
            print(f'Loan term entered: {str(UserParameters.number_of_months)} months')
        except:
            try:
                UserParameters.number_of_months = float(re.sub("[^.0-9]", "", text_input))
                self.lineEdit_2.setText(str(UserParameters.number_of_months))
            except:
                UserParameters.number_of_months = ""
                self.lineEdit_2.setText("")

    def inputbox_apr(self, text_input):
        try:
            UserParameters.apr = float(text_input) / 100
            print(f'Annual interest rate entered: {str(UserParameters.apr*100)}%')
        except:
            try:
                UserParameters.apr = float(re.sub("[^.0-9]", "", text_input))
                self.lineEdit_3.setText(str(UserParameters.apr))
            except:
                UserParameters.apr = ""
                self.lineEdit_3.setText("")

    def inputbox_tax(self, text_input):
        try:
            UserParameters.state_sales_tax = float(text_input)/ 100
            print(f'state_sales_tax entered: {str(UserParameters.state_sales_tax*100)}%')
        except:
            try:
                UserParameters.state_sales_tax = float(re.sub("[^.0-9]", "", text_input))
                self.lineEdit_4.setText(str(UserParameters.state_sales_tax))
            except:
                UserParameters.state_sales_tax = ""
                self.lineEdit_4.setText("")

    # Clear inputs and update the LineEdit box
    def clear_everything(self):
            UserParameters.warning_msgs.clear()
            UserParameters.result_msgs.clear()
            UserParameters.amount_borrowed = ()
            UserParameters.number_of_months =()
            UserParameters.apr = ()
            UserParameters.state_sales_tax = ()
            self.textBrowser_results.setText('')
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')

    def clear_stored_inputs(self):
        UserParameters.amount_borrowed = ()
        UserParameters.number_of_months =()
        UserParameters.apr = ()
        UserParameters.state_sales_tax = ()


    def append_warning_msgs(self):
        if UserParameters.warning_msgs:
            self.textBrowser_results.setText('')
            combined_warning_msgs = '\n'.join(str(i) for i in UserParameters.warning_msgs)
            self.textBrowser_results.setStyleSheet("color: red;")
            self.textBrowser_results.setText("-"*90+"\n" + combined_warning_msgs + "\n"+"-"*90)
            UserParameters.warning_msgs.clear()

    def append_result_msgs(self):
        if UserParameters.result_msgs:
            self.textBrowser_results.setText('')
            combined_result_msgs = '\n'.join(str(i) for i in UserParameters.result_msgs)
            self.textBrowser_results.setStyleSheet("color: blue;")
            self.textBrowser_results.setText("-"*90+"\n" + combined_result_msgs + "\n"+"-"*90)
            UserParameters.result_msgs.clear()

    def simulation_1(self):
        # Simulation 1 - lowering the loan term by a year.
        term =  UserParameters.real_number_of_months-12
        self.lineEdit.setText(str(UserParameters.real_amount_borrowed))
        self.lineEdit_2.setText(str(term))
        self.lineEdit_3.setText(str(UserParameters.real_apr))
        self.lineEdit_4.setText(str(UserParameters.nc_sales_tax))

    def simulation_2(self):
        # Simulation 2 - Improving credit score, lowering APR
        apr = UserParameters.real_apr*0.5
        self.lineEdit.setText(str(UserParameters.real_amount_borrowed))
        self.lineEdit_2.setText(str(UserParameters.real_number_of_months))
        self.lineEdit_3.setText(str(apr))
        self.lineEdit_4.setText(str(UserParameters.nc_sales_tax))

    def simulation_3(self):
        # Simulation 3 - Improving credit score, lowering APR and loan term
        term, apr = UserParameters.real_number_of_months-12, UserParameters.real_apr*0.5
        self.lineEdit.setText(str(UserParameters.real_amount_borrowed))
        self.lineEdit_2.setText(str(term))
        self.lineEdit_3.setText(str(apr))
        self.lineEdit_4.setText(str(UserParameters.nc_sales_tax))

    def simulation_4(self):
        # Simulation 4 - Significantly lowering APR to 6.0%
        apr = 6
        self.lineEdit.setText(str(UserParameters.real_amount_borrowed))
        self.lineEdit_2.setText(str(UserParameters.real_number_of_months))
        self.lineEdit_3.setText(str(apr))
        self.lineEdit_4.setText(str(UserParameters.nc_sales_tax))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    main()
