number_given = int(input("Give m)e your number"))
range_of_possible_divisors= range(1, number_given )
for possible_divisor in range_of_possible_divisors:
#    print (possible_divisor)
    if number_given % possible_divisor == 0:
        print (possible_divisor)