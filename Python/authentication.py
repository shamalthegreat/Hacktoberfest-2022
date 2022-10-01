#Code by hridhwesh

"""
Python program to accept username and password from user to sign-up and also run an authentication in-case the user's
already has an account in the system

Example:

Output: 
        ################################################
        Do you want to sign-up or sign-in? (1/2)
        1. Sign-up
        2. Sign-in

Input: 1

I/O :
    ################################################
    Enter username: //username inputted by user
    Enter Password: //pass inputted by user
    Confirm Password: //same pass inputted by user

Output : Successfully Signed up! 
         Redirecting to main page



"""


import time


Username = []
Password = []

def startUp():
    print("\n################################################\n")
    a=(input("Do you want to sign-up or sign-in? (1/2/3) \n 1. Sign-up \n 2. Sign-in \n 3.Terminate Program \n"))
    print("################################################")
    a=a.strip()
    
    if(a=="1"):
        signUp()
    if(a=="2"):
        signIn()
    if(a=="3"):
        return False    
    if ( a!="1" or a!="2") :
        if(a!=3):
            print("Incorrect Input!")
            startUp()          

def signUp():
    print("################################################")
    print("\nSign Up Page! \n")
    user= input("Enter username: ")
    if(user in Username):
        a=int(input("Username already exists! Press 1 to try again and 2 to sign-in\n"))
        if(a==1):
            signUp()
        if(a==2):
            signIn()
        signUp()
    passw=input("Enter password: ")
    time.sleep(1)
    conf=input("Confirm password: ")
    if (passw != conf):
        print("The passwords do not match!")
        i =int(input("Want to try again? (0 = no / 1 = yes)"))
        if (i==1):
            signUp()
        if(i!=1):
            startUp()
    
    Username.append(user)
    Password.append(passw)
    print("Successfully Signed up! \n Redirecting to main page")
    startUp()

def signIn():
    print("################################################")
    ind= None
    print("\nSign In Page! \n")
    user= input("Enter username: ")
    passw= input("Enter password: ")
    if (user not in Username):
        i = int(input("Username doesn't exist! Press 1 to try again or 0 to register \n"))
        if(i==1):
            signIn()
        if(i==0):
            signUp()
        if(i!=1 and i!=0):
            print("Incorrect choice, redirecting to main page")
            startUp()    
    ind= Username.index(user)
    if ( Password[ind] == passw):
        print("Authentication Successfull! \nRedirecting to main page.")
        startUp()
    if (Password[ind] != passw):
        print("Authentication failed. Try again!\n")
        val=int(input("Enter 0 to cancel process and any other key to try again. \n"))
        if(val==0):
            startUp()
        signIn()    



def main():
    print("################################################")
    print("\nBOOTING PROGRAM!")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    startUp()
    x=True 
    
    while (x==True):
        x= startUp()

  
main()
  
  
