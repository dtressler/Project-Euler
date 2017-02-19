

end_number = 4000000
temp_number = 1
previous_number = 1
current_number = 1
total = 0

for x in range(0, end_number):
    temp_number = current_number
    current_number += previous_number
    previous_number = temp_number
    
    if (current_number % 2 == 0):
        total += current_number

print "%d is the sum of even Fibonacci numbers up to %d" % (total, end_number)
