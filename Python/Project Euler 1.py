import math


entered_number = (input("Please enter a number: ") -1)

increments_of_three = int(math.floor(entered_number / 3))
increments_of_five = int(math.floor(entered_number / 5))

multiples_of_three = 0;
multiples_of_five = 0;

for x in range(1, increments_of_three + 1):
    amount_to_add = x * 3
    multiples_of_three += amount_to_add
	
for x in range(1, increments_of_five + 1):
    amount_to_add = x * 5
    multiples_of_five += amount_to_add
	
total = multiples_of_three + multiples_of_five

print "The sum of all the multiples of 3 and 5 below %d is %d" % (entered_number + 1, total)