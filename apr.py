class UserParameters:
    @classmethod
    def __init__(self):
        self.amount_borrowed = ()
        self.number_of_months = ()
        self.apr = ()
        self.state_sales_tax = ()
        self.warning_msgs = []
        self.result_msgs = []
        self.real_amount_borrowed = 16000
        self.real_number_of_months = 72
        self.real_apr = 24
        self.nc_sales_tax = 4.75 # North Carolina sales tax is 4.75%

class LoanCalculator:

    @classmethod
    def loan_calc(self):
        try:
            # Assuming the sales tax gets added to the loan and is not payed upfront
            loan_with_sales_tax = UserParameters.amount_borrowed*(1+UserParameters.state_sales_tax)
            monthly_payment= (loan_with_sales_tax*UserParameters.apr/12)\
                                          *((1+UserParameters.apr/12)**UserParameters.number_of_months)\
                                          /((1+UserParameters.apr/12)**UserParameters.number_of_months-1)

            total = monthly_payment * UserParameters.number_of_months
            loan_cost = total - loan_with_sales_tax

            UserParameters.result_msgs.append(f'The loan amount after tax is ${str(round(loan_with_sales_tax,2))}')
            UserParameters.result_msgs.append(f'The monthly payment after tax of {str(round(UserParameters.state_sales_tax*100,2))}% is ${str(round(monthly_payment,2))}')
            UserParameters.result_msgs.append(f'The cost of the loan with APR of {str(round(UserParameters.apr*100,2))}% for a period of {UserParameters.number_of_months} months is ${str(round(loan_cost,2))}')
            UserParameters.result_msgs.append(f'The total amount that will be payed, loan plus the cost of the loan is ${str(round(total,2))}')
        except Exception as e:
            UserParameters.warning_msgs.append(f'Error Occured : Please make sure that you filled all the fields correctly \nError Type : {e}')

user_one = UserParameters()
calc_one = LoanCalculator()
