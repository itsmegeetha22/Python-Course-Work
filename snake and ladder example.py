Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> Try AI directly in your favourite apps … Use Gemini to generate drafts and refine content, plus get Gemini Pro with access to Google's next-gen AI for ₹1,950 ₹489 for 3 months
... 1
... 100%
... import random
... 
... def dice():
...     return random.randint(1,6)
...     
... player1_name = input("Enter the player-1 name: ")
... player2_name = input("Entere the player-2 name: ")
... 
... player1_score = 0
... player2_score = 0
... 
... 
... snake = {29:15,35:21,42:12,56:22,74:39,87:3,92:64,99:44}
... ladder = {5:17,19:43,36:67,45:93,51:77,61:85,83:95}
... 
... winning_point = 100
... 
... while player1_score < winning_point and player2_score < winning_point:
... 
...     player1_status = input(f"{player1_name} - [P]lay or [Q]uit: ").upper()
...     if player1_status == 'P':
...         d=dice()
...         print("Dice score:",d)
...         if player1_score+d <= winning_point:
...             player1_score+=d
...         if player1_score in snake:
...             player1_score = snake[player1_score]
...             print(f"{player1_name}'s score: {player1_score} after snake----------")
... 
...         elif player1_score in ladder:
...             player1_score = ladder[player1_score]
            print(f"{player1_name}'s score: {player1_score} after ladder+++++++++")

        elif player1_score == winning_point:
            print(f"{player1_name}'s score: {player1_score}")
            break
            
        else:
            print(f"{player1_name}'s score: {player1_score}")
    else:
        print(f"Congrats!! {player2_name}, you won the game")
        break


    player2_status = input(f"{player2_name} - [P]lay or [Q]uit: ").upper()
    if player2_status == 'P':
        d=dice()
        print("Dice score:",d)
        if player2_score+d <= winning_point:
            player2_score+=d
        if player2_score in snake:
            player2_score = snake[player2_score]
            print(f"{player2_name}'s score: {player2_score} after snake----------")

        elif player2_score in ladder:
            player2_score = ladder[player2_score]
            print(f"{player2_name}'s score: {player2_score} after ladder+++++++++")

        elif player2_score == winning_point:
            print(f"{player2_name}'s score: {player2_score}")
            break
        else:
            print(f"{player2_name}'s score: {player2_score}")
    else:
        print(f"Congrats!! {player1_name}, you won the game")
        break
    


if player1_score > player2_score:
    print(f"Congrats!! {player1_name}, you won the game")
else:
    print(f"Congrats!! {player2_name}, you won the game")
    









