class atm(object) :
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkBalance(self):
        print("This is your balance")

    def withdrawal(self):
        print("You are withdrawing money")

def main() :
    cardNumber = input("Enter card number ")
    pinNumber  = input("Enter pin ")

    choice = int(input("Enter 1 to check balance and 2 to withdraw money. "))

    user = atm(cardNumber,pinNumber)

    if (choice == 1):
        user.checkBalance()
    elif (choice == 2):
        user.withdrawal()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

