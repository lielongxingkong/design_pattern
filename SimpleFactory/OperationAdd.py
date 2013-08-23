from Operation import Operation
class OperationAdd(Operation):
	def __init__(self):
		super
	def getResult(self):
		return self.numberA + self.numberB
if __name__ == "__main__":
	oper = OperationAdd()
	oper.numberA = 1
	oper.numberB = 2
	result = oper.getResult()
	print result
