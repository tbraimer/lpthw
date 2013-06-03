# use "def" to create function/mini script with two arguments. 
# everything indented after the colon is part of the function/mini script
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints string and pulls integer and uses modulas to pull argument
	print "You have %d cheeses!" % (cheese_count)
# prints string and pulls integer and uses modulas to pull argument
	print "You have %d boxes of crackers!" % (boxes_of_crackers)
# prints string	
	print "Man, thats enough for a party"
# prints string and goes to the next line	
	print "Get a blanket. \n"
# prints string	
print "We can just give the function numbers directly:"
# runs cheese and crackers function using 20 and 30 as arguments.
cheese_and_crackers(20, 30)
# prints strings
print "Or we can use variables from our script"
# assigns values to arguments bothe line 18 and 19
amount_of_cheese = 10
amount_of_crackers = 50
# runs function again
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# prints string
print "We can even do math inside too:"
# runs function and uses math in the arguments.
cheese_and_crackers(10 + 20, 5 + 6)
# prints string
print "And we can combine the two, variables and math:"
# run function and uses variables and math to come up with arguments.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)