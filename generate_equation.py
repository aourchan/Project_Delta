""" This formats the equation that will be displayed to the user """

def generate_equation(problem_set, coefficients = [0], constants = [0]):
	# First we determine the sign of each coefficient and constant
	coeff_signs = ['']*len(coefficients)
	const_signs = ['']*len(constants)
	for count in range(0, len(coefficients)):
		if coefficients[count] > 0:
			coeff_signs[count] = '+'
	for count in range(0, len(constants)):
		if constants[count] > 0:
			const_signs[count] = '+'
	
	if problem_set == 1:	# x + a = b
		print ('Solve for x: x') + const_signs[0] + ('%d = %d' % (constants[0], constants[1]))
	elif problem_set == 2:	# a*x + b = c
		print ('Solve for x: %dx' % coefficients[0]) + const_signs[0] + str(constants[0]) + (' = %d' % constants[1])
	elif problem_set == 3:	# a*x + b = c*x + d
		print ( ('Solve for x: %dx' % coefficients[0]) +
			const_signs[0] + ('%d = %dx' % (constants[0], coefficients[1])) +
			const_signs[1] + str(constants[1]) )
	elif problem_set == 4:	# a*x + b + c*x = d + e*x + f
		print ( ('Solve for x: %dx' % coefficients[0]) +
			const_signs[0] + str(constants[0]) +
			coeff_signs[1] + ('%dx = ' % coefficients[1]) + 
			str(constants[1]) + (coeff_signs[2]) +
			('%dx' % coefficients[2]) + (const_signs[2]) + str(constants[2]) )
	elif problem_set == 5:	# a(x + b) = c*x + d
		print ( ('Solve for x: %d(x' % coefficients[0]) + const_signs[0] +
			('%d) = %dx' % (constants[0], coefficients[1])) + const_signs[1] +
			str(constants[1]) )
	elif problem_set == 6:	# a(x + b) + c = x(d + e) + f
		print ( ('Solve for x: %d(x' % coefficients[0]) + const_signs[0] +
			str(constants[0]) + ')' + const_signs[1] + str(constants[1]) +
			(' = x(%d' % coefficients[1]) + coeff_signs[2] + str(coefficients[2]) +
			')' + const_signs[2] + str(constants[2]) )
	else:
		print "Error selecting problem set."