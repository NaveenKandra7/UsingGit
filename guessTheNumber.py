#!/bin/python

#print "Python 2"

import random

def userInput() :
	while True :
		try :
			x = int(raw_input( "Guess the number(1-99):"))
			break
		except ValueError :
			print "Not a valid number, try again"
	return x

num = random.randrange(100)
#print num
guess = userInput()
counter = 1
while guess != num :
	if num > guess :
		print "Too small, try again"
	else :
		print "Too big, try again"
        if counter < 6 :
		guess = userInput()
		counter += 1
	else :
		print "Sorry!, You loose, Its " + str(num)
		break
        #print userInput
if guess == num :
	print "Success!, You WON!!, you took " + str(counter) + " chances "
