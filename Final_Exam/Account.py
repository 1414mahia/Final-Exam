class Account:
    def __init__(self, name, email, address, account_no, initial_balance=0):
        self.name = name
        self.email = email
        self.address = address
        self.account_no = account_no
        self.balance = initial_balance
        self.loan_amount = 0
        self.transaction_history = []

    def view_detail_of_user(self):
        return f"Account No: {self.account_no}, Name: {self.name}, Email: {self.email}, Balance: {self.balance}, Loan: {self.loan_amount}, Address: {self.address}"

    def deposit_of_users(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw_of_users(self,withdraw_amount):
        if  withdraw_amount> self.balance: # total balance theke with withdraw_amount beshi hole withdraw kora jabe nh
            print("Withdrawal amount exceeded")
        else:
            self.balance -= withdraw_amount
            self.transaction_history.append(f"Withdrew: {withdraw_amount}")

    def check_balance(self):
        return f"Current Balance: {self.balance}"

    def get_transaction_history_of_users(self):
        return self.transaction_history

    def take_loan_from_bank(self, loan_amount):
        if self.loan_amount == 0: # initialy loan na niye thakle loan nite parbe
            self.loan_amount = loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
        elif self.loan_amount > 0 and self.loan_amount < 2:
            self.loan_amount += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
        
        else:
            print("you have already taken the maximum loan amount.")
            
    def transfer(self, amount, recipient_account):
        if recipient_account is None:
            print("Recipient account does not exist.")
        else:
            if amount > self.balance:
                print("Insufficient balance for transfer.")
            else:
                self.balance -= amount # balance theke transfer money minus korbo
                recipient_account.balance += amount
                self.transaction_history.append(f"Transferred: {amount} to Account {recipient_account.account_no}")
                recipient_account.transaction_history.append(f"Received: {amount} from Account {self.account_no}")

