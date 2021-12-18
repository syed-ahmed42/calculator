def calc(x, y, op):
	'''(float, float, str) -> float
	Performs the op on x and y and then returns
	the result
	'''
	#error string
	err = '\033[1;31;40mERROR: \033[0;0m'
	#Input validation
	if type(x) != float and type(y) != float:
		try:
			x = float(x)
			y = float(y)
		except ValueError:
			print(err + 'x and y must be digits')
			return -1
	if op not in ['+', '-', '*', '/']:
		print(err + 'op must be +, -, * or /')
		return -1
	
	#Calc operations
	if op == '+':
		return x + y
	elif op == '-':
		return x - y
	elif op == '*':
		return x * y
	elif op == '/':
		if y == 0:
			return -1
		return x / y


if __name__ == '__main__':
	x = input('Input x: ')
	y = input('Input y: ')
	op = input('Input operator: ')
	print(calc(x, y, op))