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
		

