class UserParameters:
    @classmethod
    def __init__(self):
        self.amount_borrowed = () # Rickey's car was approximately $16,000
        self.number_of_months = () # Rickey's loan term was around 72 months
        self.apr = () # Rickey's annual interest rate was an insane 24%
        self.state_sales_tax = () # The state sales tax in north carolina is 4.75%
        self.warning_msgs = []
        self.result_msgs = []
        self.real_amount_borrowed = 16000
        self.real_number_of_months = 72
        self.real_apr = 24
        self.nc_sales_tax = 4.75

class LoanCalculator:

    @classmethod
    def loan_calc(self):
        try:
            monthly_payment_before_tax = (UserParameters.amount_borrowed*UserParameters.apr/12)\
                                          *((1+UserParameters.apr/12)**UserParameters.number_of_months)\
                                          /((1+UserParameters.apr/12)**UserParameters.number_of_months-1)
            monthly_payment = (1+UserParameters.state_sales_tax/100)*monthly_payment_before_tax
            total = monthly_payment * UserParameters.number_of_months
            loan_cost = total - UserParameters.amount_borrowed

            #UserParameters.result_msgs.append(f'The monthly payment before tax is ${str(round(monthly_payment_before_tax,2))}')
            UserParameters.result_msgs.append(f'The monthly payment after sales tax of {str(round(UserParameters.state_sales_tax*100,2))}% is ${str(round(monthly_payment,2))}')
            UserParameters.result_msgs.append(f'The cost of the loan with APR of {str(round(UserParameters.apr*100,2))}% for a period of {UserParameters.number_of_months} months is ${str(round(loan_cost,2))}')
            UserParameters.result_msgs.append(f'The total amount that will be payed, loan plus the cost of the loan is ${str(round(total,2))}')
        except Exception as e:
            UserParameters.warning_msgs.append(f'Error Occured : Please make sure that you filled all the fields correctly \nError Type : {e}')

user_one = UserParameters()
calc_one = LoanCalculator()
