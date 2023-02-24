# #Bank Management System

bank = """
=========================================
               Welcome to 
           STATE BANK OF INDIA     
*****************************************
----- 1.Open a New Account        -------
----- 2.Withdraw Money            -------
----- 3.Deposti Money             -------
----- 4.Check Customers & Balance -------
----- 5.Exit / Quit               -------
*****************************************
"""
customers = {"ramu" : [1234,800],"somu":[2345,3000],"sabu":[4545,30000]}
while True:
    print(bank)
    option = int(input("Select your choice number from the above menu : "))
    if option==1:
        name = input("Enter your Full Name : ")
        def pin_generate(customers):
            pin = int(input("Please input a pin of your choice : "))
            if len(str(pin))==4:
                balance = int(input("Please input a value to deposit to start an account : "))
              
                customers[name]=[pin,balance]
                print("---------------------------------------------")
                print("Name : ",name)
                print("Pin : ",pin)
                print("Balance : ",balance)
                print("--Your name added to the customer system-----")
                print("--Your pin added to the customer system------")
                print("--Your balance added to the customer system--")
                print()
                print("*******New Account Created successfully******")
                print()
                print("    Note! Pleas remember the name and pin!   ")
                print("---------------------------------------------")
                key = input("Please press Enter key to go back to main menu to perform another functions or exit...")
            else:
                print("Please enter 4 digits pin !")
                pin_generate(customers)
        pin_generate(customers)
    elif option==2:
        print("Choice number 2 is selected by the customer")
        def check_name(customers):
            name=input("Please input name : ")
            if name in customers:
                def check_pin(customers):
                    pin = int(input("Please input pin : "))
                    if pin==customers[name][0]:
                        print("Your current balance : ",customers[name][1],"/Rs")
                        print()
                        print()
                        def draw_amount(customers):
                            withdraw = int(input("Input value to withdraw : "))
                            if withdraw>customers[name][1]:
                                print("#####Insufficient balance#####")
                                print()
                                print("******************************")
                                draw_amount(customers)
                            else :
                                customers[name][1]-=withdraw
                                money=customers[name][1]
                                
                                print()
                                print("------Withdraw Successful-------")
                                print("Your new Balance : ",customers[name][1],"-/Rs")
                                print()
                                print()
                                key = input("Please press Enter key to go back to main menu to perform another functions or exit...")
                        draw_amount(customers)
                    else : 
                        print("enter valid Pin!")
                        check_pin(customers)
                check_pin(customers)
                    
            else : 
                print("Please enter valid user name! ")
                check_name(customers)
        check_name(customers)
    elif option==3:
        print("Choice number 3 is selected by the customer")
        def check_name(customers):
            name=input("Please input name : ")
            if name in customers:
                def check_pin(customers):
                    pin = int(input("Please input pin : "))
                    if pin==customers[name][0]:
                        print("Your current balance : ",customers[name][1],"/Rs")
                        print()
                        print()
                        deposit = int(input("Input value to deposit : "))
                        customers[name][1]+=deposit
                        print()
                        print("------Deposit Successful-------")
                        print("Your new Balance : ",customers[name][1],"-/Rs")
                        print()
                        print()
                        key = input("Please press Enter key to go back to main menu to perform another functions or exit...")
                    else : 
                        print("enter valid Pin!")
                        check_pin(customers)
                check_pin(customers)
                    
            else : 
                print("Please enter valid user name! ")
                check_name(customers)
        check_name(customers)
    elif option==4:
        print("Choice number 4 is selected by the customer")
        def check_name(customers):
            name=input("Please input name : ")
            if name in customers:
                def check_pin(customers):
                    pin = int(input("Please input pin : "))
                    if pin==customers[name][0]:
                        print("="*33)
                        print("Your current balance : ",customers[name][1],"/Rs")

                        print()
                        key = input("Please press Enter key to go back to main menu to perform another functions or exit...")
                    else : 
                        print("enter valid Pin!")
                        check_pin(customers)
                check_pin(customers)
                    
            else : 
                print("Please enter valid user name! ")
                check_name(customers)
        check_name(customers)
        # for i in customers:
        #     print("Name : ",i)
        #     print("Balance : ",customers[i][1],"-/Rs")
        #     print()
        key = input("Please press Enter key to go back to main menu to perform another functions or exit...")
    elif option==5:
        print("Choice number 5 is selected by the customer ")
        print("Thank you for using SBI banking system!")
        print()
        print()
        print("Come again")
        print("Bye Bye")
        break
    else : 
        print("Please enter valid option!")

    