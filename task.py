#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction. 
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 

#With every simulation step the orentation should be corrected, applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

import random as rd

class Flight:

	def __init__(self):
		self.angle = 0

	def correct_angle(self):
		higher = True
		if self.angle < 0:
			higher = False
		if higher:
			self.angle += -(rd.random() * rd.randint(0, int(self.angle)))
		else:
			self.angle += -(rd.random() * rd.randint(int(self.angle), 0))
	
	def turbolation(self):
		self.angle += rd.random() * rd.randint(-3, 3)

	
if __name__ == '__main__':
		
	flight = Flight() 
	while(True):

		flight.turbolation()

		print("Flight angle is " + str(flight.angle))

		flight.correct_angle()

		print("Flight angle corrected to " + str(flight.angle))
		
