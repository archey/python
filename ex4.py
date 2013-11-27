#Variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#subtracts two variables cars - drivers or 100 - 30
cars_not_driven = cars - drivers
#creates a new variable called cars_driven from the value of the drivers variable
cars_driven = drivers
#multiplies cars_driven * space_in_a_car or 30 * 4.0
carpool_capacity = cars_driven * space_in_a_car
#divides the passengers / cars_driven or 90 / 30
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
