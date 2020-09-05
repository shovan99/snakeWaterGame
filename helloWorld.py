import random
total_limit=10
current_limit=0
computer_point=0
your_point=0
while(current_limit<total_limit):
            print("press 's' for snake, press 'w' for water and press 'g' for gun")
            userInput=input()
            list=["s","w","g"]
            s=random.choice(list)
            if userInput==s:
                print("Tied")
                your_point+=1
                computer_point+=1
                print(your_point)
                print(computer_point)
                current_limit+=1
                print("Remaining limit:",(total_limit-current_limit))
            elif userInput=="s" and s=="w":
                print("computer wins this point")
                computer_point += 2
                print(your_point)
                print(computer_point)
                current_limit += 1
                print("Remaining limit:", (total_limit-current_limit))
            elif userInput=="s" and s=="g":
                        print("computer wins this point")
                        computer_point += 2
                        print(your_point)
                        print(computer_point)
                        current_limit += 1
                        print("Remaining limit:", (total_limit-current_limit))
            elif userInput=="w" and s=="s":
                        print("you wins this point")
                        your_point += 2
                        print(your_point)
                        print(computer_point)
                        current_limit += 1
                        print("Remaining limit:", (total_limit-current_limit))
            elif userInput=="g" and s=="w":
                        print("computer wins this point")
                        computer_point += 2
                        print(your_point)
                        print(computer_point)
                        current_limit += 1
                        print("Remaining limit:", (total_limit-current_limit))
            elif userInput=="w" and s=="g":
                        print("you wins this point")
                        your_point += 2
                        print(your_point)
                        print(computer_point)
                        current_limit += 1
                        print("Remaining limit:", (total_limit-current_limit))
            elif userInput=="g" and s=="s":
                        print("you wins this point")
                        your_point += 2
                        print(your_point)
                        print(computer_point)
                        current_limit += 1
                        print("Remaining limit:", (total_limit-current_limit))
if your_point>computer_point:
    print("You are the winner")
elif computer_point>your_point:
    print("Sorry!! computer wins the game.")
else:print("Match Tied !!!")
print("Game Over")







