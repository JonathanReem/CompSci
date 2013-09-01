price = float(raw_input("Price of Meal (in dollars): "))
tip_percent = float(raw_input("percent to tip: ")) / 100
tip = price * tip_percent
print "You should tip " + str(tip)