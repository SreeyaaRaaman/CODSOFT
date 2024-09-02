import random
options=["Rock","Paper","Scissors"]
countuser=0
countcomputer=0
while(True):
    user_choice=input("Choose Rock,Paper or Scissors:")
    computer_choice=random.choice(options)
    print("Your choice:",user_choice)
    print("computer choice:",computer_choice)
    if user_choice==computer_choice:
        print("It's a tie!")
    elif user_choice=="Rock" and computer_choice=="Scissors":
        print("You win!")
        countuser=countuser+1
    elif user_choice=="Scissors" and computer_choice=="Paper":
        print("You win!")
        countuser=countuser+1
    elif user_choice=="Paper" and computer_choice=="Rock":
        print("You win!")
        countuser=countuser+1
    else:
        print("Computer wins!")
        countcomputer=countcomputer+1
    print("\nFINAL SCORES\nuser",countuser,"\ncomputer",countcomputer)
    play=input("Do you want to play again?(y/n):")
    if play!="y":
        break
        
        
    
