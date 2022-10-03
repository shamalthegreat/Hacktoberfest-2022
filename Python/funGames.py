#code by Hridhwesh

"""
Python code to play 3 kinds of games. Responsive and user-friendly!

Example :

Output: 
        ###############################################
        Would game would you like to play? :D
        1.Truth Or Dare
        2.Would You Rather
        3.Never Have I Ever
        4.Exit

Input:  1

Output:
        ###############################################
        TRUTH OR DARE!
        1.Press 1 for a Truth Question
        2.Press 2 for a Dare Question

Input:     1

Output:
        Question:  What is the next skill that you'd like to learn really well?
        Wanna go again? (1=Yes/0=No)

Input:     0

//Program restarts from beginning
"""


from tracemalloc import start
import requests
import json

truth= "https://api.truthordarebot.xyz/v1/truth"
dare="https://api.truthordarebot.xyz/api/dare"
WYR="https://api.truthordarebot.xyz/api/wyr"
NHIE="https://api.truthordarebot.xyz/api/nhie"

def TruthOrDare():
    print("###############################################")
    x= int(input("TRUTH OR DARE!\n1.Press 1 for a Truth Question\n2.Press 2 for a Dare Question\n"))
    if (x==1):
        try:
            r = requests.get(truth)
            r.raise_for_status()
            print("Question: ", r.json()['question'])    
            z=int(input("Wanna go again? (1=Yes/0=No)"))
            if(z==1):
                TruthOrDare()
            if(z==0):
                startUp()
            else:
                print("\nInvalid Input!\nReverting to main page!") 
                startUp()

        except requests.exceptions.HTTPError as err:
            print( SystemExit(err))
            print("Oops! System error! Please pick again!")
            TruthOrDare()
    if (x==2):
        try:
            r = requests.get(dare)
            r.raise_for_status()
            print("Question: ", r.json()['question']) 
            z=int(input("Wanna go again? (1=Yes/0=No)"))
            if(z==1):
                TruthOrDare()
            if(z==0):
                startUp()
            else:
                print("\nInvalid Input!\nReverting to main page!") 
                startUp()
        except requests.exceptions.HTTPError as err:
            print( SystemExit(err))
            print("Oops! System error! Please pick again!")
            TruthOrDare()
    else:
        print("Invalid Input! Try again.")

def WouldYouRather():
    print("###############################################")      
    print("WOULD YOU RATHER!") 
    try:
            r = requests.get(WYR)
            r.raise_for_status()
            print("Question: ", r.json()['question'])
            z=int(input("Wanna go again? (1=Yes/0=No)"))
            if(z==1):
                WouldYouRather()
            if(z==0):
                startUp()
            else:
                print("\nInvalid Input!\nReverting to main page!") 
                startUp()
    except requests.exceptions.HTTPError as err:
            print( SystemExit(err))
            print("Oops! Server Timed out. Trying again!")
            WouldYouRather()
            
                

def NeverHaveIEver():
    print("###############################################") 
    print("NEVER HAVE I EVER")
    try:
            r = requests.get(NHIE)
            r.raise_for_status()
            print("Question: ", r.json()['question'])
            z=int(input("Wanna go again? (1=Yes/0=No)"))
            if(z==1):
                NeverHaveIEver()
            if(z==0):
                startUp()
            else:
                print("\nInvalid Input!\nReverting to main page!") 
                startUp()
    except requests.exceptions.HTTPError as err:
            print( SystemExit(err))
            print("Oops! Server Timed out. Trying again!")
            NeverHaveIEver()

def startUp():
    print("###############################################")
    x= int(input("Would game would you like to play? :D\n1.Truth Or Dare\n2.Would You Rather\n3.Never Have I Ever\n4.Exit Game\n"))
    if(x==1):
        TruthOrDare()
    if (x==2):
        WouldYouRather()    
    if(x==3):
        NeverHaveIEver()
    if(x==4):
        print("Program Terminated")
        exit()    
    else:
        print("Invalid Input, try again!")    
        startUp()

startUp()