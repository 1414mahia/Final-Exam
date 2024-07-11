from Bank import Bank
    # Create a bank instance
bank = Bank()

    # Create accounts
bank.create_account_in_bank("Kalam", "kalam@gmail.com", "Chittagong", 1, 1000)
bank.create_account_in_bank("Boby", "boby24@gmail.com", "Comilla", 2, 500)

    # Show all accounts
print("Accounts created:")
bank.show_users_account()

    # Deposit into Kalam's account
bank.deposit_in_bank(1, 500)

    # Withdraw from Boby's account
bank.withdraw_in_bank(2, 200)

    # Check balance of Kalam's account
bank.check_balance_in_bank(1)

    # Take a loan from Boby's account
bank.take_loan_in_bank(2, 1000)
