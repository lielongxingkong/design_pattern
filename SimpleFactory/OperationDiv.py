from Operation import Operation
class OperationDiv(Operation):
	def __init__(self):
		super
	def getResult(self):
		result = 0
		try:
			result = float(self.numberA) / float(self.numberB)
		except Exception as e:
			print e
		finally:
			return result

if __name__ == "__main__":
	oper = OperationDiv()
	oper.numberA = 1
	oper.numberB = 2
	result = oper.getResult()
	print result
