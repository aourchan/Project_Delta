from random import randrange 
"""This function generates problems from specified problem sets."""

# This provides the feedback when the user answers correctly
def correct_feedback():
	fb = ["Correct! Great job!", "Awesome! You got it!"]
	print fb[randrange(0, 2)]

# This provides the feedback when the user answers incorrectly
def incorrect_feedback():
	fb = ["Shoot. Not quite. Try another one.", "You missed this one, but try another."]
	print fb[randrange(0, 2)]

# problem_set_1: x - 4 = 6, x + 4 = 6
def problem_set_1():
	lhs = randrange(-10, 11)
	while lhs == 0:
		lhs = randrange(-10, 11)
	rhs = randrange(-10, 11)
	while rhs == 0:
		rhs = randrange(-10, 11)
 
	# Print the prompt for a user input and accept user input
	if lhs < 0:
		print "Solve for x: x - %d = %d" % (-lhs, rhs)
	elif lhs > 0:
		print "Solve for x: x + %d = %d" % (lhs, rhs)
 
	correct_answer = rhs - lhs
	user_answer = float(raw_input("-> "))
 
	# Check user answer
	if user_answer == correct_answer:
		print "Correct! Excellent job!"
	elif user_answer == rhs + lhs:
		print "I think you made one of the common mistakes with this problem set."
		print "Try another problem."
	else:
		print "Not quite. Let's try another problem."

# Need to think about way to make it so the user doesn't have to enter fractions in.
# Or only have clean divisible answers
# problem_set_2: 5x + 6 = 7x - 2
def problem_set_2():
	lhs_x = randrange(-10, 11)
	while lhs_x == 0:
		lhs_x = randrange(-10, 11)
 
	lhs_const = randrange(-10, 11)
	while lhs_const == 0:
		lhs_const = randrange(-10, 11)
 
	rhs_x = randrange(-10, 11)
	while rhs_x == 0:
		rhs_x = randrange(-10, 11)
 
	rhs_const = randrange(-10, 11)
	while rhs_const == 0:
		rhs_const = randrange(-10, 11)
 
	# Print the prompt for a user input and accept user input
	if lhs_const < 0 and rhs_const < 0:
		print "Solve for x: %dx - %d = %dx - %d" % (lhs_x, -lhs_const, rhs_x, -rhs_const)
	elif lhs_const > 0 and rhs_const < 0:
		print "Solve for x: %dx + %d = %dx - %d" % (lhs_x, lhs_const, rhs_x, -rhs_const)
	elif lhs_const < 0 and rhs_const > 0:
		print "Solve for x: %dx - %d = %dx + %d" % (lhs_x, -lhs_const, rhs_x, rhs_const)
	else:
		print "Solve for x: %dx + %d = %dx + %d" % (lhs_x, lhs_const, rhs_x, rhs_const)
 
	correct_answer = (rhs_const - lhs_const) / (lhs_x - rhs_x)
	user_answer = float(raw_input("-> "))
 
	# Check user answer
	if user_answer == correct_answer:
		print "Correct! Excellent job!"
	elif (user_answer == (rhs_const + lhs_const) / (lhs_x - rhs_x)) or \
		 (user_answer == (rhs_const + lhs_const) / (lhs_x + rhs_x)) or \
		 (user_answer == (rhs_const - lhs_const) / (lhs_x + rhs_x)):
		print "I think you made one of the common mistakes with this problem set."
		print "Try another problem."
	else:
		print "Not quite. Let's try another problem."

#problem_set_1()
#problem_set_2()
#incorrect_feedback()