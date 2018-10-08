from random import *
print("-------------------------------------")
print("  Welcome to the UP OR DOWN GAME!")
print("-------------------------------------")

choice=input("""Choose your level
@@@@@@@@@@@@@@@
|Easy 	   : 0|
|Mid-Level : 1|
|Hard	   : 2|
|Expert	   : 3|
@@@@@@@@@@@@@@@

""")
if choice == 0 :
	number=randrange(10)
if choice == 1 :
	number=randrange(100)
if choice == 2 :
	number=randrange(1000)
if choice == 3 :
	number=randrange(10000)
print("Now guess a number")
guess=input()
if number==guess :
	print("Congratulations,the number was "+str(number)+"!")
while number != guess:
 if number > guess :
	print("Up")
	newguess=input()
	if newguess <= guess:
		print("Oh God,I said up.Guess again!")
		newguess=input()
		if newguess <= guess:
			print("Ok i get it.You don't know the meaning of Up")
			print("Good Bye")
		else:
			guess=newguess
	else :
			guess=newguess
	if number == guess :
		print("Congratulations,the number was "+str(number)+"!")
 if number < guess :
	print("Down")
	newguess=input()
	if newguess >= guess:
		print("Oh God,I said up.Guess again!")
		newguess=input()
		if newguess >= guess:
			print("Ok i get it.You don't know the meaning of Down")
			print("Good Bye")
		else:
			guess=newguess
	else :
			guess=newguess
	if number == guess :
		print("Congratulations,the number was "+str(number)+"!")

