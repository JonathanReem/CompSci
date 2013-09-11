A = int(raw_input("Enter Side A: "))
B = int(raw_input("Enter Side B: "))
C = int(raw_input("Enter Side C: "))

comparison_A = A >= B + C
comparison_B = B < A + C
comparison_C = C >= A + B

"""
If a triangle can be constructed, then:
comparison_A, comparison_B, comparison_C == True, False, True

As a result, the end goal of the program is to detect if any of
these are not their correct value.

Some critical facts (by algebra):

If B is False, then it is certain that EITHER:
	A is True OR
	C is True

If A is True, then it is certain that:
	B is False (Because A is larger than B + C, 
				A must be larger than B)
	C is False (Because A is larger than C + B,
				A must be larger than C)

If C is True, then it is certain that:
	B is False (Because C is larger than A + B,
				C must be larger than B)
	A is False (Because C is larger than A + B,
				C must be larger than A)

Therefore, the only possible cases are:
(In the form ABC where T = True, F = False)

FTF <-- A triangle can be formed.

TFF <-- A is too large
FFT <-- C is too large

Therefore, only in the correct configuration (because TFT
is impossible) will comparison_A != comparison_B and 
comparison_C != comparison_B.

Therefore the following series of comparisons will yield
the correct result:
"""

compare_first_two = comparison_A != comparison_B
compare_last_two = comparison_B != comparison_C

print compare_first_two == compare_last_two

"""
The only cases that this can return true in are:

TFT
FTF

TFT would only be possible if simulatenously C > A and A > C
a clear impossible situation. Therefore, it only returns true
if the configuration of comparison_A, comparison_B, and comparison_C
is FTF, or the correct configuration. QED.

Also, boring, one line solution: (Ethan figured this out also)

print max(A, B, C) > A + B + C - max(A, B, C)

"""