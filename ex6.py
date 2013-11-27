# creates a variable called x prints the formatter string %d with value 10
x = "There are %d types of people." % 10
#creates a variable called binary with a value of binary
binary = "binary"
#creates a variable called do_not with a value of don't
do_not = "don't"
#creates  a variable called y and prints the fromatter string of %s and %s with the values of binary and do_not variables
y = "Those who know %s and those who %s." % (binary, do_not)

#prints the variable x 
print x
#prints the variable y
print y

#prints the string formatter %r with the value of the x variable
print "I said: %r." % x
#prints the string formatter %s with the value of the y variable
print "I also said: '%s'." % y

#creates variable hiliarious with value false
hiliarious = False
#creates variable joke_evaluaiton and asks a question with the hiliarious variable
joke_evaluation = "Isn't that joke so funny?! %r"

#prints the sum of the variables hiliarious and joke_evalution
print joke_evaluation % hiliarious

#creates a variable w with a statement 
w = "This is the left side of..."
#creates a variable e with a statement
e = "a string with a right side."

#prints the sum of variable w + e it also adds the two sum together to form one string value
print w + e
