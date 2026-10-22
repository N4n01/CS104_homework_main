import random
'''comp = "rock"'''
wins = 0
loses = 0
draws = 0
rounds = 1
player = 'a'
while player != "q" :
    comp = random.randint(1, 3)
    if comp == 1 :
        comp = "rock"
    elif comp == 2 :
        comp = "paper"
    else :
        comp = "scissors"

    print(f"Round {rounds}")

    try :
        player = str(input("rock, paper, scissors or q to quit: "))
        if player == "rock" and comp == "scissors" :
            output = 'You win!'
        elif player == "paper" and comp == "rock" :
            output = 'You win!'
        elif player == "scissors" and comp == "paper" :
            output = 'You win!'

        elif player == "rock" and comp == "paper" :
            output = 'Computer wins!'
        elif player == "paper" and comp == "scissors" :
            output = 'Computer wins!'
        elif player == "scissors" and comp == "rock" :
            output = 'Computer wins!'

        elif player == comp :
            output = 'Draw!'
        else :
            output = 'Invalid choice'
    except ValueError :
        output = 'Invalid choice'

    if output != 'Invalid choice' :
        print(f"Computer: {comp}")
        rounds += 1
    if player != "q" :
        print(output)

    if output == 'You win!' :
        wins += 1
    elif output == 'Computer wins!' :
        loses += 1
    elif output == 'Draw!' :
        draws += 1
    if player == "q" :
        print(f"Played {rounds-1} round(s)")
        print(f"You won {wins}, the computer won {loses}, draws: {draws}")
