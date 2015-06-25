
user_answer = raw_input("->")

if "/" in user_answer:
	print "Index of slash = %d" % user_answer.index("/")
	print "Top number = %f" % float(user_answer[0:user_answer.index("/")])
	print "Bot number = %f" % float(user_answer[user_answer.index("/")+1:])
	print "Divided number = %f" % (float(user_answer[0:user_answer.index("/")])/float(user_answer[user_answer.index("/")+1:]))