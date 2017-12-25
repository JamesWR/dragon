def primary(X):
	x = float(X*100.0)
	red = (1.0 - (0.02 * x)) if x < (100.0/2.0) else  0.0
	blue = 0 if x < (100.0/2.0) else (0.02 * x)-1.0
	green = (0.02 * x) if x < (100.0/2.0) else (2 - (0.02 * x))
	return red, blue, green

def lessPrimary(X):
	x = float(X*100.0)
	scalar = (0.01 * x)
	red = (1.0 - scalar) if (scalar < 0.5) else 0.5
	blue = 0.5 if (scalar < 0.5) else 0.0 + scalar
	green = (0.5 + scalar) if (scalar < 0.5) else 0.5
	return red, blue, green

def bounce(X):
	x = float(X*100.0)
	if x % 2 < 1:
		return 1.0, 0, 0
	else:
		return 0, 1.0 , 0

def test():
	for i in range(1,101):
		print(lessPrimary(i/100.0))
# test()