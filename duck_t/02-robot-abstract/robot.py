import wpilib
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):

	def robotInit(self):
		"""
		Create joystick object, four motor controllers, and a MecanumDrive class.
		"""
	
	def teleopPeriodic(self):
		"""
		Pair the joystick with the motors. 
		"""

if __name__ == "__main__":
	wpilib.run(MyRobot)