from Account import Account
class Bank:
    def __init__(self):
        self.total_available_balance = 0
        self.total_loan = 0
        self.loan_status = "off"
        self.accounts = []

    def create_account_in_bank(self, name, email, address, account_no, initial_balance):
        new_account = Account(name, email, address, account_no, initial_balance)
        self.accounts.append(new_account)  #account list a new account append korbo
        self.total_available_balance += initial_balance #total balance er sathe initial balance add korbo
        print(f"Account created for {name} with initial balance {initial_balance}")

    def delete_account_in_Bank(self, account_no):
        for account in self.accounts:
            if account.account_no == account_no:# accounts theke j account delete korbo ta bahir kore anbo
                self.total_available_balance -= account.balance # account er balance o total balance theke delete korbo
                self.total_loan -= account.loan_amount # same vabeh loan o delete korbo
                self.accounts.remove(account)  # finally remove korbo
                print(f"Account No {account_no} deleted")
                return
        print(f"Account No {account_no} does not exist.")

    def show_users_account(self):
        if not self.accounts:
            print("No accounts exist.")
        else:
            for account in self.accounts:
                print(account.view_detail_of_user())

    def show_total_balance_in_bank(self):
        print(f"Total Balance: {self.total_available_balance}")

    def show_total_loan_in_bank(self):
        print(f"Total Loan: {self.total_loan}")

    def off_loan(self):
        self.loan_status = "off"
        print("Loan status turned off")

    def on_loan(self):
        self.loan_status = "on"
        print("Loan status turned on")

    def deposit_in_bank(self, account_no, amount):
        for account in self.accounts:
            if account.account_no == account_no:
                account.deposit_of_users(amount) # bank a user er money deposit korbo
                self.total_available_balance += amount
                print(f"Deposited {amount} to Account No {account_no}.")
                return
            

    def withdraw_in_bank(self, account_no, amount):
        for account in self.accounts:
            if account.account_no == account_no:
                account.withdraw_of_users(amount) 
                self.total_available_balance -= amount
                return
      

    def check_balance_in_bank(self, account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                print(account.check_balance())
                return
       
    def check_transaction_history_in_bank(self, account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                print(account.get_transaction_history())
                return
           
    def take_loan_in_bank(self, account_no, loan_amount): # banker total loan er hishab
        for account in self.accounts:
            if account.account_no == account_no:
                account.take_loan_from_bank(loan_amount)
                self.total_loan += loan_amount
                return
       # print(f"Account No {account_no} does not exist.")

    def transfer_in_bank(self, from_account_no, to_account_no, amount):
        sender = None # shuru te sender and recipient null thakbe
        recipient = None
        for account in self.accounts: 
            if account.account_no == from_account_no: # account no er sathe from account no mile gele send hobe
                sender = account
            elif account.account_no == to_account_no:
                recipient = account

        if sender is None or recipient is None: # sender and recipient both null hole
            print("One or both accounts do not exist.")
        else:
            sender.transfer(amount, recipient)




    