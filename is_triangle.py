# Jonathan Reem
# Septemeber 10, 2013
# Determines if sides A, B, and C can form a triangle.

A = int(raw_input("Enter Side A: "))
B = int(raw_input("Enter Side B: "))
C = int(raw_input("Enter Side C: "))

# One line solution: (Ethan also got this)
print max(A, B, C) > A + B + C - max(A, B, C)