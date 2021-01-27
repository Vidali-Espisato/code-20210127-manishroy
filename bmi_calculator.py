
class Calculator:
	ranges = {
				(0, 18.5): ("Underweight", "Malnutrition risk"),
				(18.5, 25): ("Normal weight", "Low risk"),
				(25, 30): ("Overweight", "Enhanced risk"),
				(30, 35): ("Moderately obese", "Medium risk"),
				(35, 40): ("Severely obese", "High risk"),
				(40, 100): ("Very severely obese", "Very high risk")
			}
	
	def __init__(self, weight, height):
		self.height = height / 100
		self.weight = weight
		self.bmi = self.calculate()

	def calculate(self):
		bmi = round(self.weight / (self.height ** 2))
		self.category, self.risk = self.ranges[list(filter(lambda x: x[0] <= bmi < x[1], self.ranges))[0]]
		return bmi

	# def get_category(self):
	# 	return self.category
	
	# def get_risk(self):
	# 	return self.risk

