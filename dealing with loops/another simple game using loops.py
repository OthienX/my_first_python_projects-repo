import random , syd
import sys

print("ROCK, SCISSORS, PAPER")
#these variables keep the number of wins, loses and ties
win = 0
lose =0
ties =0
while True:
    print("%swins, %slose, %sties", "(wins, lose, ties)")
    while True:
        print("enter your move rock(r), paper(p), scissors(s) or quit(q)")
        play_move =input()
        if player_move == q:
            sys.exit()
        if play_move ==r or play_move ==p or play_move ==s:
            break
        print("type one of r, p, s or q")
        if play_move ==r:
             print("ROCK versus................")
        if play_move ==p:
             print("PAPER versus..............")
        if play_move == s:
           print("SCISSOR versus...................")
#displaying what the computer chose
        random_number = random.randint(1,3)
        if random_number==1:
            computer_move = "r"
            print("ROCK")
        elif random_number ==2:
            computer_move ="p"
            print("PAPER")
        elif random_number ==3:
            computer_move ="s"
            print("SCISSOR")
  # displaying and recording of wins, losses and ties
          if play_move ==computer_move:
            print("its a ties")
            ties = ties+1
          elif play_move =="r" and computer_move =="s":
            print("you win")
            wins =wins+1
          elif play_move =="p" and computer_move =="r":
            print("you win ")
            wins = wins+1
          elif play_move =="s" and computer_move =="p":
            print("you win")
            wins = wins +1
          elif play_move =="r" and computer_move == "p":
              print("you lose")
              lose = lose+1
          elif play_move =="p" and computer_move =="s":
              print("you lose")
              lose = lose+1
          elif play_move =="s" and computer_move =="r":
              print("you lose")
              lose = lose+1


