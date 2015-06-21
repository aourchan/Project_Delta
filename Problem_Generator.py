"""This function generates problems from specified problem sets."""


from random import randrange
from feedback import *
from generate_equation import generate_equation


# Global variables
Prompt = "Your Answer-> "	# Prompt that will be ask user for their response
correct_score = 1			# Value of getting a correct answer
common_mis_score = 0.5		# Value of getting a common mistake answer
incorrect_score = 0			# Value of getting an incorrect answer

# problem_set_1: x + a = b
# const_lhs = a, const_rhs = b
def problem_set_1():
	print 'Problem Set 1'
	problem_set = 1
	# First we generate the constants
	const_lhs = randrange(-10, 11)
	while const_lhs == 0:
		const_lhs = randrange(-10, 11)
	const_rhs = randrange(-10, 11)
	while const_rhs == 0:
		const_rhs = randrange(-10, 11)
	correct_answer = const_rhs - const_lhs
	coefficients = [0]
	constants = [const_lhs, const_rhs]
 
	# Now we print the problem to the user and prompt the user for a response
	generate_equation(problem_set, coefficients, constants)
	user_answer = int(raw_input(Prompt))
 
	# Check user answer and provide feedback
	if user_answer == correct_answer:
		correct_feedback()
		return correct_score
	elif (user_answer == const_rhs + const_lhs) or (user_answer == -correct_answer):
		common_mistake_feedback(user_answer, correct_answer)
		return common_mis_score
	else:
		incorrect_feedback(user_answer, correct_answer)
		return incorrect_score
		
# problem_set_2: a*x + b = c
# coeff_lhs = a
# const_lhs = b, const_rhs = c
# constant_total = c - b
def problem_set_2():
	print 'Problem Set 2'
	problem_set = 2
	# First we ensure that the correct answer is a whole number.
	correct_answer = randrange(-8, 9)
	while correct_answer == 0:
		correct_answer = randrange(-8, 9)
	
	# Now we derive the x coefficient
	coeff_lhs = randrange(-8, 9)
	coefficients = [coeff_lhs]
	
	# Next we derive the constants on each side of the equation.
	constant_total = correct_answer * coeff_lhs
	const_lhs = randrange(-8, 9)
	while const_lhs == 0:
		const_lhs = randrange(-8, 9)
	const_rhs = constant_total + const_lhs
	constants = [const_lhs, const_rhs]
	
	# Now we print the problem to the user and prompt the user for a response
	generate_equation(problem_set, coefficients, constants)
	user_answer = int(raw_input(Prompt))
	 
	# Check user answer and provide feedback
	if user_answer == correct_answer:
		correct_feedback()
		return correct_score
	elif (user_answer == (const_rhs + const_lhs) / coeff_lhs) or \
		 (user_answer == -correct_answer):
		common_mistake_feedback(user_answer, correct_answer)
		return common_mis_score
	else:
		incorrect_feedback(user_answer, correct_answer)
		return incorrect_score
	

# problem_set_3: a*x + b = c*x + d
# coeff_lfs = a, coeff_rhs = c
# const_lhs = b, const_rhs = d
# constant_total = d - b
# coefficient_total = a - c
def problem_set_3():
	print 'Problem Set 3'
	problem_set = 3
	# First we ensure that the correct answer is a whole number.
	correct_answer = randrange(-8, 9)
	while correct_answer == 0:
		correct_answer = randrange(-8, 9)

	# Now we derive the x coefficients on each side of the equation.
	coefficient_total = randrange(-8, 9)
	while coefficient_total == 0:
		coefficient_total = randrange(-8, 9)
	coeff_rhs = randrange(-8, 9)
	while coeff_rhs == 0 or ((coeff_rhs + coefficient_total) == 0):
		coeff_rhs = randrange(-8, 9)
	coeff_lhs = coefficient_total + coeff_rhs
	coefficients = [coeff_lhs, coeff_rhs]
	 
	# Next we derive the constants on each side of the equation.
	constant_total = coefficient_total * correct_answer
	const_lhs = randrange(-8, 9)
	while const_lhs == 0 or ((const_lhs + constant_total) == 0):
		const_lhs = randrange(-8, 9)
	const_rhs = constant_total + const_lhs
	constants = [const_lhs, const_rhs]

	# Now we print the problem to the user and prompt the user for a response
	generate_equation(problem_set, coefficients, constants)
	user_answer = int(raw_input(Prompt))
	 
	# Check user answer and provide feedback
	if user_answer == correct_answer:
		correct_feedback()
		return correct_score
	elif (user_answer == (const_rhs + const_lhs) / (coeff_lhs - coeff_rhs)) or \
		 (user_answer == (const_rhs + const_lhs) / (coeff_lhs + coeff_rhs)) or \
		 (user_answer == (const_rhs - const_lhs) / (coeff_lhs + coeff_rhs)) or \
		 (user_answer == -correct_answer):
		common_mistake_feedback(user_answer, correct_answer)
		return common_mis_score
	else:
		incorrect_feedback(user_answer, correct_answer)
		return incorrect_score

# problem_set_4: a*x + b + c*x = d + e*x + f
# coeff_1 = a, coeff_2 = c, coeff_3 = e
# const_1 = b, const_2 = d, const_3 = f
# coefficient_total = a + c - e
# constant_total = d + f - b
def problem_set_4():
	print 'Problem Set 4'
	problem_set = 4
	# First we ensure that the correct answer is a whole number
	correct_answer = randrange(-8, 9)
	while correct_answer == 0:
		correct_answer = randrange(-8, 9)
	
	# Now we derive the x coefficients on each side of the equation
	coefficient_total = randrange(-8, 9)
	while coefficient_total == 0:
		coefficient_total = randrange(-8, 9)
	coeff_1 = randrange(-8, 9)
	coeff_2 = randrange(-8, 9)
	while coeff_1 == 0 or coeff_2 == 0 or ((coeff_1 + coeff_2 - coefficient_total) == 0):
		coeff_1 = randrange(-8, 9)
		coeff_2 = randrange(-8, 9)
	coeff_3 = coeff_1 + coeff_2 - coefficient_total
	coefficients = [coeff_1, coeff_2, coeff_3]
	
	# Next we derive the constants on each side of the equation
	constant_total = correct_answer * coefficient_total
	const_2 = randrange(-8, 9)
	const_3 = randrange(-8, 9)
	while const_2 == 0 or const_3 == 0 or ((const_2 + const_3 - constant_total) == 0):
		const_2 = randrange(-8, 9)
		const_3 = randrange(-8, 9)
	const_1 = const_2 + const_3 - constant_total
	constants = [const_1, const_2, const_3]
	
	# Now we print the problem to the user and prompt the user for a response
	generate_equation(problem_set, coefficients, constants)
	user_answer = int(raw_input(Prompt))
	
	# Check user answer and provide feedback
	if user_answer == correct_answer:
		correct_feedback()
		return correct_score
	elif (user_answer == (const_1 + const_2 + const_3) / (coeff_1 + coeff_2 + coeff_3)) or \
		(user_answer == -correct_answer):
		common_mistake_feedback(user_answer, correct_answer)
		return common_mis_score
	else:
		incorrect_feedback(user_answer, correct_answer)
		return incorrect_score

# problem_set_5: a(x + b) = c*x + d
# coeff_lhs = a, coeff_rhs = c
# const_lhs = b, const_rhs = d
# coefficient_total = a - c
# constant_total = d - a*b
def problem_set_5():
	print 'Problem Set 5'
	problem_set = 5
	# First we ensure that the correct answer is a whole number
	correct_answer = randrange(-8, 9)
	while correct_answer == 0:
		correct_answer = randrange(-8, 9)
	
	# Now we derive the x coefficients on each side of the equation
	coefficient_total = randrange(-8, 9)
	while coefficient_total == 0:
		coefficient_total = randrange(-8, 9)
	coeff_lhs = randrange(-8, 9)
	while coeff_lhs == 0 or ((coeff_lhs - coefficient_total) == 0):
		coeff_lhs = randrange(-8, 9)
	coeff_rhs = coeff_lhs - coefficient_total
	coefficients = [coeff_lhs, coeff_rhs]
	
	# Next we derive the constants on each side of the equation
	constant_total = correct_answer * coefficient_total
	const_lhs = randrange(-8, 9)
	while const_lhs == 0 or ((coeff_lhs * const_lhs + constant_total) == 0):
		const_lhs = randrange(-8, 9)
	const_rhs = coeff_lhs * const_lhs + constant_total
	constants = [const_lhs, const_rhs]
	
	# Now we print the problem to the user and prompt the user for a response
	generate_equation(problem_set, coefficients, constants)
	user_answer = int(raw_input(Prompt))
	
	# Check user answer and provide feedback
	if user_answer == correct_answer:
		correct_feedback()
		return correct_score
	elif (user_answer == (const_rhs + coeff_lhs * const_lhs) / (coeff_lhs - coeff_rhs)) or \
		(user_answer == (const_rhs - coeff_lhs * const_lhs) / (coeff_lhs + coeff_rhs)) or \
		(user_answer == -correct_answer):
		common_mistake_feedback(user_answer, correct_answer)
		return common_mis_score
	else:
		incorrect_feedback(user_answer, correct_answer)
		return incorrect_score

# problem_set_6: a(x + b) + c = x(d + e) + f
# coeff_1 = a, coeff_2 = d, coeff_3 = e
# const_1 = b, const_2 = c, const_3 = f
# coefficient_total = a - d - e
# constant_total = f - a*b - c
def problem_set_6():
	print 'Problem Set 6'
	problem_set = 6
	# First we ensure that the correct answer is a whole number
	correct_answer = randrange(-8, 9)
	while correct_answer == 0:
		correct_answer = randrange(-8, 9)
	
	# Now we derive the x coefficients on each side of the equation
	coefficient_total = randrange(-8, 9)
	while coefficient_total == 0:
		coefficient_total = randrange(-8, 9)
	coeff_1 = randrange(-8, 9)
	coeff_2 = randrange(-8, 9)
	while coeff_1 == 0 or coeff_2 == 0 or ((coeff_1 - coeff_2 - coefficient_total) == 0):
		coeff_1 = randrange(-8, 9)
		coeff_2 = randrange(-8, 9)
	coeff_3 = coeff_1 - coeff_2 - coefficient_total
	coefficients = [coeff_1, coeff_2, coeff_3]
	
	# Next we derive the constants on each side of the equation
	constant_total = correct_answer * coefficient_total
	const_1 = randrange(-8, 9)
	const_2 = randrange(-8, 9)
	while const_1 == 0 or const_2 == 0 or ((const_1 * coeff_1 + const_2 + constant_total) == 0):
		const_1 = randrange(-8, 9)
		const_2 = randrange(-8, 9)
	const_3 = const_1 * coeff_1 + const_2 + constant_total
	constants = [const_1, const_2, const_3]
	
	# Now we print the problem to the user and prompt the user for a response
	generate_equation(problem_set, coefficients, constants)
	user_answer = int(raw_input(Prompt))
	
	# Check user answer and provide feedback
	if user_answer == correct_answer:
		correct_feedback()
		return correct_score
	elif (user_answer == (const_1 + const_2 + const_3) / (coeff_1 + coeff_2 + coeff_3)) or \
		(user_answer == -correct_answer):
		common_mistake_feedback(user_answer, correct_answer)
		return common_mis_score
	else:
		incorrect_feedback(user_answer, correct_answer)
		return incorrect_score
