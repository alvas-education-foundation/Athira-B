def login():
    for i in range (0,3):
        x= input("Enter your name ")
        y=input("Enter your password ")

        if x== "Micheal" and y== "e3$WT89x":
           return( print("Login Successful"))
            
        else:
            print("Invalid username or password")
    return(print("Account Locked"))

login()


