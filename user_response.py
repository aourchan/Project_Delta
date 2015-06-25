""" This function:
	(1) Prompts the user for a response
	(2) Checks the type of the user response
	(3) If user responded with appropriate type passes user response on
	(4) Else If the user responded in an inappropriate manner asks for another prompt
	(5) If new prompt is still incorrect type then print out user score info and quit"""

# This function is looking for an integer response from the user
def user_response():
	# Prompt that will be ask user for their response
	Prompt = "Your Response-> "
	# Number of times that we have tried to get a type appropriate user answer
	try_count = 0
	# Number of times that we want to try to get a type appropriate user answer before quitting
	try_max = 2
	# True when user gives a type appropriate response
	good_response = False
	
	while try_count <= try_max:
		# Get the user response
		user_answer = raw_input(Prompt)
		
		# Check if quit command was initiated by user
		if user_answer == 'q' or user_answer == 'Q':
			quit()
		
		# Check if user entered a fraction in a/b format
		if "/" in user_answer:
			user_answer = float(user_answer[0:user_answer.index("/")]) / float(user_answer[user_answer.index("/")+1:])
		
		# Check if the user answer is an int
		try:
			user_answer = int(user_answer)
			return user_answer
		except ValueError:
			# If value is not an int check if value is float
			try:
				user_answer = float(user_answer)
				return user_answer
			except ValueError:
				# If value is also not a float then prompt user for new response
				try_count = try_count + 1
				if try_count > try_max:
					print "You didn't enter a number again, we will quit for now."
					quit()
				else:
					print "Oops, it seems like you didn't enter a number. Try again."
	
	
# This function is looking for a string response from the user	
def user_response_string():
	temp = 1