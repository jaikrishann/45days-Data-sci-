name = input('Enetr your name')
print(f"hello {name}")

print("how may i help you","\n")


message = """Please select any of the option
    Type 1 >>> CHECK BALANCE,
    Type 2 >>> DEPOSIT,
    Type 3 >>> WITHDRAWl"""

print(message , "\n")

task= int(input("Enter your choice:"))
available_balance = 5000
if (task >= 1) & (task <= 3):
    if task == 1:
        print(f"Your current balance is: {available_balance}")
    elif task == 2:
        deposit_amount = int(input("Enter the amount to deposit: "))
        available_balance += deposit_amount
        print(f"Deposit successful, your new balance is: {available_balance}")
    else:
        withdrawal_amount = int(input("Enter the amount to withdraw: "))
        if withdrawal_amount <= available_balance:
            available_balance -= withdrawal_amount
            print(f"Withdrawal successful, your new balance is: {available_balance}")
        else:
            print("Insufficient balance")
