"""	This function is what will run and call for new problems.
	It also keeps track of the user's score for each problem set.
	After a certain number of questions the function will prompt the user 
	to see if they would like more questions."""


from Problem_Generator import *


problem_set_1_total = 0		# Initial score of user on problem_set_1
problem_set_2_total = 0		# Initial score of user on problem_set_2
problem_set_3_total = 0		# Initial score of user on problem_set_3
problem_set_4_total = 0		# Initial score of user on problem_set_4
problem_set_5_total = 0		# Initial score of user on problem_set_5
problem_set_6_total = 0		# Initial score of user on problem_set_6
problem_set_1_count = 0		# Initial count of user on problem_set_1
problem_set_2_count = 0		# Initial count of user on problem_set_2
problem_set_3_count = 0		# Initial count of user on problem_set_3
problem_set_4_count = 0		# Initial count of user on problem_set_4
problem_set_5_count = 0		# Initial count of user on problem_set_5
problem_set_6_count = 0		# Initial count of user on problem_set_6
keep_going = True			# Initialization of keep_going
number_of_questions = 6		# Initial number of questions that the user will be asked
user_score = 0				# Initial user score combining scores from all problem sets
count = 1					# Counter of what number question user is on
temp_score = 0				# Temporarily stores the score on the latest user problem

print 'We are going to start off with %s questions and we will go from there. Good luck!' % number_of_questions
while keep_going:
	if count == 1:
		temp_score = problem_set_1()
		if temp_score == 1:
			problem_set_1_total = problem_set_1_total + 1
		user_score = 10 * temp_score + user_score
		problem_set_1_count = problem_set_1_count + 1
	elif count == 2:
		temp_score = problem_set_2()
		if temp_score == 1:
			problem_set_2_total = problem_set_2_total + 1
		user_score = 10 * temp_score + user_score
		problem_set_2_count = problem_set_2_count + 1
	elif count == 3:
		temp_score = problem_set_3()
		if temp_score == 1:
			problem_set_3_total = problem_set_3_total + 1
		user_score = 10 * temp_score + user_score
		problem_set_3_count = problem_set_3_count + 1
	elif count == 4:
		temp_score = problem_set_4()
		if temp_score == 1:
			problem_set_4_total = problem_set_4_total + 1
		user_score = 10 * temp_score + user_score
		problem_set_4_count = problem_set_4_count + 1
	elif count == 5:
		temp_score = problem_set_5()
		if temp_score == 1:
			problem_set_5_total = problem_set_5_total + 1
		user_score = 10 * temp_score + user_score
		problem_set_5_count = problem_set_5_count + 1
	elif count == 6:
		temp_score = problem_set_6()
		if temp_score == 1:
			problem_set_6_total = problem_set_6_total + 1
		user_score = 10 * temp_score + user_score
		problem_set_6_count = problem_set_6_count + 1
	else:
		# Here we want to choose a question based on the user score.
		# Not sure if we want to start off the bat with one of each question or what.
		if user_score >= 57:
			temp_score = problem_set_6()
			if temp_score == 1:
				problem_set_6_total = problem_set_6_total + 1
			user_score = 10 * temp_score + user_score
			problem_set_6_count = problem_set_6_count + 1
		elif user_score >= 50:
			temp_score = problem_set_5()
			if temp_score == 1:
				problem_set_5_total = problem_set_5_total + 1
			user_score = 10 * temp_score + user_score
			problem_set_5_count = problem_set_5_count + 1
		elif user_score >= 40:
			temp_score = problem_set_4()
			if temp_score == 1:
				problem_set_4_total = problem_set_4_total + 1
			user_score = 10 * temp_score + user_score
			problem_set_4_count = problem_set_4_count + 1
		elif user_score >= 30:
			temp_score = problem_set_3()
			if temp_score == 1:
				problem_set_3_total = problem_set_3_total + 1
			user_score = 10 * temp_score + user_score
			problem_set_3_count = problem_set_3_count + 1
		elif user_score >= 20:
			temp_score = problem_set_2()
			if temp_score == 1:
				problem_set_2_total = problem_set_2_total + 1
			user_score = 10 * temp_score + user_score
			problem_set_2_count = problem_set_2_count + 1
		else:
			temp_score = problem_set_1()
			if temp_score == 1:
				problem_set_1_total = problem_set_1_total + 1
			user_score = 10 * temp_score + user_score
			problem_set_1_count = problem_set_1_count + 1
	if count == number_of_questions:
		print 'Your current score on each problem set is:'
		print 'Problem Set 1: %d correct out of %d questions' % (problem_set_1_total, problem_set_1_count)
		print 'Problem Set 2: %d correct out of %d questions' % (problem_set_2_total, problem_set_2_count)
		print 'Problem Set 3: %d correct out of %d questions' % (problem_set_3_total, problem_set_3_count)
		print 'Problem Set 4: %d correct out of %d questions' % (problem_set_4_total, problem_set_4_count)
		print 'Problem Set 5: %d correct out of %d questions' % (problem_set_5_total, problem_set_5_count)
		print 'Problem Set 6: %d correct out of %d questions' % (problem_set_6_total, problem_set_6_count)
		print 'Your total score is %d out of %d possible' % (user_score, number_of_questions * 10)
		print 'Would you like some more practice problems? Enter how many questions you would like.'
		user_answer = raw_input('-> ')
		if user_answer.isdigit() and user_answer != '0':
			number_of_questions = number_of_questions + int(user_answer)
		else:
			keep_going = False
	count = count + 1
	