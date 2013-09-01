name = raw_input("Enter your first and last name: ")
first_name = name.split()[0]
last_name = name.split()[1]
age = int(raw_input("Enter your age: "))
print "Your first name has " + str(len(first_name)) + " letters"
print "Your last name has " + str(len(last_name)) + " letters"
print "Next year you will be " + str(age + 1) + " years old"