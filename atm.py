correct_pin = "26092002"    # user PIN
attempts = 3            # allowed attempts

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Login successful!\n")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN! Attempts left: {attempts}")

if attempts == 0:
    print("Account locked! Too many wrong attempts.")
    exit()

# ===== Show ATM Menu After PIN Success =====
print("=== ATM System ===")
print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")
balance = 5000  # starting balance

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your Balance: ₹{balance}\n")

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn: ₹{amount}")
            print(f"Remaining Balance: ₹{balance}\n")
        else:
            print("Insufficient balance!\n")

    elif choice == "3":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited: ₹{amount}")
        print(f"Updated Balance: ₹{balance}\n")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Try again.\n")
