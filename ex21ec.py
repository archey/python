#creates  a function called add and it adds a + b then returns the answer
def add(a,b):
	print "ADDING %d +%d" % (a,b)
	return a+b

#creates a function called subtract and subtracts a - b then returns the answer
def subtract(a,b):
	print "SUBTRACTING %d -%d" % (a,b)
	return a-b

#creates a function called multiply and multiplies a * b then returns the answer
def multiply(a,b):
	print "MULTIPLYING %d*%d" % (a,b)
	return a*b
#creates a function called divide and divides a / b then returns the answer
def divide(a,b):
	print "DIVIDING %d/%d" % (a,b)
	return a/b

print "Let's do some math with just functions:"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Let's take a stab at the extra credit"

#sum = (24 + 34 / 100) (- 1032)
#print "%d" % sum

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is the a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

sum = (35 + (74 - (180 * (50 / 2) ) ) )

print "The extra credit answer is %d!" % sum
