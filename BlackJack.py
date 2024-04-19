import random

Deck = []
UserCards = []
MyCards = []
InputFilePath = "BlackJack.txt"

ifh = open(InputFilePath, "r", encoding = "utf-8")
Deck = []
for line in ifh:
			Deck.append(line.strip())
print(Deck)

print()

Prompt = "Press Enter To Get Cards, E = Enough:"
while True: 
	Choice = input(Prompt).upper()
	if Choice == "E":
		break
	elif Choice == "":
		random.shuffle(Deck)
		c = Deck[-1]
		UserCards.append(c)
		for c in UserCards:
			print(c, end = " ")
		UserSum = 0
		for c in UserCards:
			if c[0] in ('J', 'Q', 'K'):
				UserSum = UserSum + 10
			elif c[0] in ('2', '3', '4', '5', '6', '7', '8', '9'):
				UserSum = UserSum + int(c[0])
			elif c[0] == '1' and c[1] == '0':
				UserSum = UserSum + 10
			else:
				if UserSum <= 10:
					UserSum = UserSum + 11
				else:
					UserSum = UserSum + 1
		print(UserSum)
		if UserSum > 21:
			print("You Lose!")
			quit()
		elif UserSum == 21:
			print("BlackJack!")
			quit()
		else:
			continue
	else:
		print("Unknown Choice")
print()
while True:
	random.shuffle(Deck)
	MyCards.append(Deck[-1])
	for c in MyCards:
		print(c, end = " ")
	MySum = 0
	for c in MyCards:
		if c[0] in ('J', 'Q', 'K'):
			MySum = MySum + 10
		elif c[0] in ('2', '3', '4', '5', '6', '7', '8', '9'):
			MySum = MySum + int(c[0])
		elif c[0] == '1' and c[1] == '0':
			MySum = MySum + 10
		else:
			if MySum <= 10:
				MySum = MySum + 11
			else:
				MySum = MySum +1
	print(MySum)
	if MySum > 21:
		print("You Win!")
		quit()
	elif MySum > UserSum:
		print("You Lose!")
		quit()
	else:
		continue