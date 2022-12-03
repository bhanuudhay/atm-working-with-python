
print("""
    **********
    * Welcome*
    **********
      """)
#take input from user
h=int(input("""
          1 Owner Info
          2 Project Details
          3 Proceed to project\n
          """))
if h==1:
    print("""
          Name: Bhanu Udhay Singh
          Regd no: 12203053
          Section: K22FG
          Roll no: 71
          """)
elif h==2:
    print("""
             Project Name: Replicate the working of ATM for a single user
             
             Working:
             Like for any user who has already successfully logged
             into his/her account on the ATM Machine, now we will program
             the next steps he may want to perform like Display the balance
             Withdraw the Money and Deposit the money
             """)
print("\nATM WORKING PROJECT")
print("WELCOME TO DSH BANK")
name=input("Enter your name:")
bal=int(input("Enter your balance(must be above 5000):"))
pin=int(input("Enter your pin:"))
x=1
#if bal less than 5000 loop will end
if bal>5000:
    if pin==1234:
        print("HELLO",name,"Your current balance is:",bal)
        while x==1:
            c=int(input("""
            Press
            1.Check Balance
            2.Deposit
            3.Withdrawl
            4.Exit\n"""))
            if c==1:
                print("\nYour Balance is:",bal)
            elif c==2:
                d=int(input("\nAmount You Want To Deposit:"))
                bal=bal+d
                print("Your Updated Balance:",bal)              
            elif c==3:
                d=int(input("\nAmount You Want To Withdraw:"))
                bal=bal-d
                print("\nYour Updated Balance:",bal)
            else:
                print("Thank You")
                exit(0)
    else:
        print("!!!!Wrong Pin!!!!")
else:
    print("Insufficient Balance")

            
