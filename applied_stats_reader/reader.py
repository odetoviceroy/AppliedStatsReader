# George Juarez - AMAT465
# Sample Reader for Textbook Data
# Sample code works in Python 2.7

import sys

# Usage: python reader.py inputfile command
# python reader.py inputfile X x_value

x_vals = []
y_vals = []

def readFile(finp):
	with open(finp) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	for line in content:
		line_arr = line.split(" ")
		y_vals.append(float(line_arr[0]))
		x_vals.append(float(line_arr[4]))

def sum_x(): # sum x values obvs
	return sum(x_vals)

def sum_sq_x(): # square all values of x and sum them
	return sum([ex ** 2 for ex in x_vals])

def sum_y(): # sum y values obvs
	return sum(y_vals)

def sum_sq_y():	# square all values of y and sum them
	return sum([why ** 2 for why in y_vals])

def mean_x(): # find mean of x obvs
	if(len(x_vals) > 0):
		return sum(x_vals)/len(x_vals)
	return -1

def mean_y(): # find mean of y obvs
	if(len(x_vals) > 0):
		return sum(y_vals)/len(x_vals)
	return -1

def sum_x_times_y(): # sum up all values of x[i] * y[i]
	counter = 0
	sum_x_times_y = 0
	for ex in x_vals:
		sum_x_times_y += ex * y_vals[counter]
		counter += 1
	return sum_x_times_y

def calc_beta_one():
	num = (len(x_vals) * sum_x_times_y()) - (sum_x() * sum_y())
	denom = (len(x_vals) * sum_sq_x()) - (sum_x() * sum_x())
	return num/denom

def calc_beta_zero():
	return mean_y() - (calc_beta_one() * mean_x())

def expected_y(ex):
	return calc_beta_zero() + (calc_beta_one() * float(ex))

def calc_sec():
	if(len(x_vals) > 0):
		return sum_sq_x() - (sum_x() * sum_x()/len(x_vals))
	return -1

def calc_sse():
	if(len(x_vals) > 0):
		sec = sum_sq_y() - ((sum_y() * sum_y()) / len(x_vals))
		return sec - (calc_beta_one() * calc_beta_one()) * (calc_sec())
	return -1		

def print_all():
	counter = 0
	print "Row   X    Y"
	for ex in x_vals:
		print counter + 1, " ", ex, "  ", y_vals[counter]
		counter += 1

def print_help():
	with open("help.txt") as f:
		content = f.readlines()
	for c in content:
		print c,

def main():
	
	if(len(sys.argv) == 2):
		if(sys.argv[1] == "help"):
			print_help()
	if(len(sys.argv) > 2):
		readFile(sys.argv[1])

		if(sys.argv[2] == "print-table"):
			print_all()
		if(sys.argv[2] == "print-results"):
			print "N: ", len(x_vals), "\nSum of X values: ", sum_x(), "\nSum of Y values: ", sum_y()
			print "Sum of X times Y values: ", sum_x_times_y(), "\nSum of X^2 values:", sum_sq_x(), "\nSum of Y^2 values: ", sum_sq_y()
			print "Mean X values: ", mean_x(), "\nMean Y values: ", mean_y()
			print "Max X value: ", max(x_vals), "\nMin X value:", min(x_vals), "\nMax Y value: ", max(y_vals), "\nMin Y value: ", min(y_vals)
			print "Beta[1]: ", calc_beta_one(), "\nBeta[0]: ", calc_beta_zero()
			print "Regression Equation: Y =", calc_beta_zero(), "+", calc_beta_one(), "* X"
			print "SSE: ", calc_sse()
			print calc_sec()
		if(len(sys.argv) > 2):
			if(sys.argv[2].lower() == "x"):
				print expected_y(sys.argv[3])

if __name__  == "__main__":
	main()
