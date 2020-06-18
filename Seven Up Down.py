import random
print("Welcome to 7 up down")
name=input("Enter your name: ")
print("Hello "+name)
coins=5000
print("You have currently 5000 coins. Use it wisely")
x = "y"

while x == "y":
    bet=int(input("Place your bet: "))
    if(coins==0):
        print("You dont have enough coins..please Restart the game!!!")
        break
    else:
        if(bet>coins):
            print("You dont have "+bet+" coins.")
        else:
            print("\n\nIf you win,You will get double the bet.")
            print("But if you lose,You will lose amount equal to bet from coins.\n")
            print("Press 1 if your choice is from 2 to 6")
            print("Press 2 if your choice is 7")
            print("Press 3 if your choice is from 8 to 12\n")
            choice=int(input("Enter your choice: "))
            number = random.randint(2,12) 

            if number == 2:
                print("----------   ----------")
                print("|        |   |         |")
                print("|   O    |   |    O    |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 3:
                print(" ----------    ----------")
                print("|         |    |         |")
                print("| O    O  |    |    O    |")
                print("|         |    |         |")
                print("-----------    ----------")
            elif number == 4:
                print("----------   ----------")
                print("|        |   |         |")
                print("| O    O |   |  O   O  |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 5:
                print("----------   ----------")
                print("|        |   |         |")
                print("|O  O  O |   |  O   O  |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 6:
                print("----------   ----------")
                print("|        |   |         |")
                print("|O  O  O |   | O  O  O |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 7:
                print("----------   ----------")
                print("| O    O  |   |         |")
                print("|         |   | O  O  O |")
                print("| O    O  |   |         |")
                print("----------   ----------")
            elif number == 8:
                print("----------   ----------")
                print("| O    O  |  | O    O  |")
                print("|         |  |         |")
                print("| O    O  |  | O    O  |")
                print("----------   ----------")
            elif number == 9:
                print("----------   ----------")
                print("|O     O |   | O    O |")
                print("|   O    |   |        |")
                print("|O     O |   | O    O |")
                print("----------   ----------")
            elif number == 10:
                print("----------   ----------")
                print("| O    O |  | O     O  |")
                print("|    O   |  |    O     |")
                print("| O    O |  | O     O  |")
                print("----------   ----------")
            elif number == 11:
                print("----------   ----------")
                print("| O    O  |   | O    O |")
                print("| O    O  |   |   O    |")
                print("| O    O  |   | O    O |")
                print("----------   ----------")
            else: 
                print("----------   ----------")
                print("| O    O |   |  O    O |")
                print("| O    O |   |  O    O |")
                print("| O    O |   |  O    O |")
                print("----------   ----------")
                
            if((choice==1 and number<7)or (choice==2 and number==7)or (choice==3 and number>7)):
                coins+=bet*2
                print("LUCKY ROLL")
                    
            else:
                coins-=bet
                print("TRY AGAIN")
        print("You have currently "+str(coins)+" coins.")
        x = input("Press y to roll again: ")
            
