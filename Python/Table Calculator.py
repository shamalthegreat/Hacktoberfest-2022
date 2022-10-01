import time
user_calculates = True
while user_calculates:
    num = int(input("Tell me The Number for which tables you want.\n"))
    print("Here's Your Table!")
    for i in range (1,11):
        print(f"{num} x {i} = {num*i}")
    user_choice = input("Do You Want to Calculate The Table Again?? [Y/N]: ")
    if user_choice == "y":
        user_calculates = True
    elif user_choice == "n":
        user_calculates = False
        break
    else:
        print("Invalid Command, Please Try Again...")
        time.sleep(5)
        user_calculates = False
