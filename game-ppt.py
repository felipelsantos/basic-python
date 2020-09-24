#!/usr/bin/env python3

import random
import time

print("=" * 35)
print("Let's play \033[1;37mRock\033[m - \033[1;32mPaper\033[m - \033[1;36mScissors\033[m")
print("=" * 35)

print("""
Choose:
0 = Quit
1 = \033[1;37mRock\033[m
2 = \033[1;32mPaper\033[m
3 = \033[1;36mScissors\033[m""")

moves = [1,2,3]

win = 0
lost = 0
tie = 0

x = 0
while x == 0:
	player = int(input("\nChoose your move: "))
	pc = random.choice(moves)

	if player == 0:
		print("Quit game\n")
		break

	if player == pc:
		time.sleep(1)
		print("\033[1;32mA Tie, try again\033[m")
		tie += 1

	if player == 1 and pc == 2:
		time.sleep(1)
		print("Player=\033[1;37mRock\033[m \nPC=\033[1;32mPaper\033[m \n\033[1;31mYou lost, try again\033[m")
		lost += 1

	if player == 2 and pc == 3:
		time.sleep(1)
		print("Player=\033[1;32mPaper\033[m \nPC=\033[1;36mScissors\033[m \n\033[1;31mYou lost, try again\033[m") 
		lost += 1

	if player == 3 and pc == 1:
		time.sleep(1)
		print("Player=\033[1;36mScissors\033[m \nPC=\033[1;32mPaper\033[m \n\033[1;31mYou lost, try again\033[m")
		lost += 1

	if player == 3 and pc == 2:
		time.sleep(1)
		print("Player=\033[1;36mScissors\033[m \nPC=\033[1;32mPaper\033[m \n\033[1;34mYou win\033[m")
		win += 1

	if player == 2 and pc == 1:
		time.sleep(1)
		print("Player=\033[1;32mPaper\033[m \nPC=\033[1;37mRock\033[m \n\033[1;34mYou win\033[m")
		win += 1

	if player == 1 and pc == 3:
		time.sleep(1)
		print("Player=\033[1;37mRock\033[m \nPC=\033[1;36mScissors\033[m \n\033[1;34mYou win\033[m")
		win += 1

	if player not in moves:
		print("Choose a valid option")

print("=" * 12)
print("===RESULT===")
print("=" * 12)
print("WINS = {} ".format(win))
print("DEFEATS = {} ".format(lost))
print("TIES = {} ".format(tie))
