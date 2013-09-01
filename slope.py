x1 = float(raw_input("x1 = "))
y1 = float(raw_input("y1 = "))
x2 = float(raw_input("x2 = "))
y2 = float(raw_input("y2 = "))

slope = (y2 - y1) / (x2 - x1)
print "The slope is " + str(slope)

b = y2 - slope * x2
print "The equation of the line is Y = " + str(slope) + "X + " + str(b) 