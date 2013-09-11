cents = int(raw_input("Input a number of cents: "))

num_quarters = cents // 25
cents_left = cents - num_quarters * 25

num_dimes = cents_left // 10
cents_left -= num_dimes * 10

num_nickels = cents_left // 5
cents_left -= num_nickels * 5

num_pennies = cents_left

print cents, " cents is ", num_quarters, " quarters, ", num_dimes, " dimes, ", num_nickels, " nickels, and ", num_pennies, " pennies."