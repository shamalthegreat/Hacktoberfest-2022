from logo import art as art
import random

def game():
    highScore = 10
    r = random.randint(1, 100)
    count = 0
    print(art)
    print("\nGuess number between 1 to 100 : ")
    while True:
        count += 1
        num = int(input("Enter number here : "))
        if num > 100:
            print("\nGuess number smaller than 100")
        elif num < r:
            print("Higher number..")
            print("\nGuess again!")
        elif num > r:
            print("Lower number..")
            print("\nGuess again!")
        else:
            print(f"\nCorrect!..  You guessed in {count} attempts")
            if count < highScore:
                print(f"Previous highscore was : {highScore}")
                print(f"New highscore is : {count}")
                highScore = count
            if count > highScore:
                print(f"Previous highscore was : {highScore}")
                break
            break

def restart():
    a = 0
    while True:
        if a == 0:
            game()
            a=a+10
        b = int(input("\nDo you want to play again ? (1 for ""YES"" / 2 for ""NO"") : "))
        if b == 2:
            print("\n\tThank you for playing!!\n\n")
            break
        elif b == 1:
            game()


restart()
