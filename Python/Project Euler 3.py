num = input("Please enter the number you would "
           "like to find the largest prime of: ")


def prime_check(number): #checks if current iteration is a prime
    for x in range(2, number):
        if number % x == 0:
            return 0

#starts from the input and works down
for x in range(num, 2, -1): 
    #when prime_check doesn't return 0 it has found a prime
    if prime_check(x) != 0:
        print "%d is the largest prime!" % (x)
        break
    else:
        continue