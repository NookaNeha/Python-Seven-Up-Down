import random                #importing random module
print("Welcome to 7 up down")  # starting game
name=input("Enter your name: ")       # get the name and
print("Hello "+name)                  # greet the person
coins=5000
print("You have currently 5000 coins. Use it wisely")
x = "y"

while x == "y":
    bet=int(input("Place your bet: "))      #Take bet as input
    if(coins==0):                                                                       #check if player has enough coins.
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
            choice=int(input("Enter your choice: "))        #Take the choice
            number = random.randint(2,12) 

            if number == 2:                                   #Roll the dice according to the number
                print("----------   ----------")
                print("|        |   |         |")
                print("|   O    |   |    O    |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 3:                                 #Roll the dice according to the number
                print(" ----------    ----------")
                print("|         |    |         |")
                print("| O    O  |    |    O    |")
                print("|         |    |         |")
                print("-----------    ----------")
            elif number == 4:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("|        |   |         |")
                print("| O    O |   |  O   O  |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 5:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("|        |   |         |")
                print("|O  O  O |   |  O   O  |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 6:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("|        |   |         |")
                print("|O  O  O |   | O  O  O |")
                print("|        |   |         |")
                print("----------   ----------")
            elif number == 7:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("| O    O  |   |         |")
                print("|         |   | O  O  O |")
                print("| O    O  |   |         |")
                print("----------   ----------")
            elif number == 8:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("| O    O  |  | O    O  |")
                print("|         |  |         |")
                print("| O    O  |  | O    O  |")
                print("----------   ----------")
            elif number == 9:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("|O     O |   | O    O |")
                print("|   O    |   |        |")
                print("|O     O |   | O    O |")
                print("----------   ----------")
            elif number == 10:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("| O    O |  | O     O  |")
                print("|    O   |  |    O     |")
                print("| O    O |  | O     O  |")
                print("----------   ----------")
            elif number == 11:                                 #Roll the dice according to the number
                print("----------   ----------")
                print("| O    O  |   | O    O |")
                print("| O    O  |   |   O    |")
                print("| O    O  |   | O    O |")
                print("----------   ----------")
            else:                                  #Roll the dice according to the number
                print("----------   ----------")
                print("| O    O |   |  O    O |")
                print("| O    O |   |  O    O |")
                print("| O    O |   |  O    O |")
                print("----------   ----------")
                
            if((choice==1 and number<7)or (choice==2 and number==7)or (choice==3 and number>7)):              #check if player won
                coins+=bet*2
                print("LUCKY ROLL")
                    
            else:
                coins-=bet
                print("TRY AGAIN")
        print("You have currently "+str(coins)+" coins.")
        x = input("Press y to roll again: ")          #ask to play again
            
