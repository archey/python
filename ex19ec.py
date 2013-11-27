def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
def soda_and_candy(soda_count, candy_boxes):
	print "Your have %d sodas!" % soda_count
	print "You have %d boxes of candy!" % candy_boxes
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give our function numbers directly:"
soda_and_candy(50, 60)

print "Or, we can use variables from our scripts:"
amount_of_soda = 20
amount_of_candy = 60

soda_and_candy(amount_of_soda, amount_of_candy)

print "Let's do some math:"
soda_and_candy(50+30, 80-10)


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our scripts:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
