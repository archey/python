name = 'Tyler S. Bennett'
age = 24 # not  a lie
height = 68 # inches
inches = 68
cm = inches * 2.54 # cinemeters
weight = 165 # lbs
eyes = 'Green'
teeth = 'White'
hair = 'Black'

print "Let's talke about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "Tyler is %d inches tall and in centimeters he is %d cm tall." % (inches, cm)
# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
