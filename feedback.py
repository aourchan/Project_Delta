"""This file provides feedback to the user """


from random import randrange


# This provides the feedback when the user answers correctly
def correct_feedback():
	fb = [	"Correct! Great job!", 
			"Awesome! You got it!"]
	print fb[randrange(0, len(fb))]

# This provides the feedback when the user answers in a commonly mistaken manner
def common_mistake_feedback(user_answer, correct_answer):
	fb = [	"I think you made one of the common mistakes with this problem set. Try another",
			"Shoot. It seems like you might have made a common mistake. Check your work. Let's try another"]
	print fb[randrange(0, len(fb))]
	print "Your answer x = %d" % user_answer
	print "The correct answer was x = %d" % correct_answer

# This provides the feedback when the user answers incorrectly
def incorrect_feedback(user_answer, correct_answer):
	fb = [	"Shoot. Not quite. Try another one.",
			"You missed this one, but try another."]
	print fb[randrange(0, len(fb))]
	print "Your answer x = %d" % user_answer
	print "The correct answer was x = %d" % correct_answer