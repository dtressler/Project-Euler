end_number = input("Input the number you would like to find "
                   "the even Fibonacci numbers of: ")
temp_number = 1
previous_number = 1
current_number = 1
total = 0

for x in range(0, end_number):
    #temp_number holds the value of the current_number
    temp_number = current_number
    #adds previous_number to current_number for next value
    current_number += previous_number
    #updates previous number
    previous_number = temp_number
    
    #finds even Fibonacci numbers and adds them to total
    if (current_number % 2 == 0):
        total += current_number

print "%d is the sum of even Fibonacci numbers up to %d" % (total, end_number)
