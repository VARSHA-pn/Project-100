class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account

    def balance(self):
        print('total BALANCE: ₹ 10000')

    def cashwithdrawl(self, amount):
        new_amount = 10000 - amount
        print("You have withdrawn amount "+str(amount) + ". Your remaining balance is "+ str(new_amount))
        
        def main():
            print("Welcome to Marvel bank !")
            Account= input("Enter your account no. ")
            cardnumber= input("Enter your CardNo. ")
            pin= input("Enter your pin ")

            user =  Atm(Account,cardnumber,pin)

            print("Choose your action")
            print("1.Balance  2.Withdrawl")
            activity = int(input("Enter activity number :- "))
            
            if (activity == 1):
                user.check_balance()
            elif (activity == 2):
                print("money")


            if (choose == 1):
                money = int(input("Enter the amount:- "))
                user.withdrawl(money)

           else:
            print("Enter a valid number")

            main()



