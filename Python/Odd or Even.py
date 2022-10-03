while True:
     number = int(input("Which number do you want to check? "))
     if number % 2 == 0:
          print("This is an Even Number")
     else:
          print("This is a Odd Number")
     again = input("Would You Like to Check More Numbers? {Y/N}\n").lower()
     if again == "y":
          continue
     elif again == "n":
          break
     else:
          print("Invalid Input")


