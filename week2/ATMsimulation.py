choice=1
balance=0
while choice==1:
    option=int(input("Choose an option  (1.Deposit 2.Withdraw 3.balance\n"))

    if option==1:
        balance=balance+int(input("Enter the amout you want to deposit\n"))
    elif option==2:
        balance=balance-int(input("Enter the amount to withdraw\n"))
    else:
        print(balance)
    choice=int(input("press 1 to continue 0 to exit\n"))
if choice==0:
    print("Transaction ended successfully")