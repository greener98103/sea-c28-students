def fibonacci(n):
###Returns the fibonacci series based off a user defined number
 	global _fibonacci
    if n == 0:
	    return 0
    elif n == 1:
        return 1
    else:
		return fibonacci(n-1)+fibonacci(n-2)
### lucas numbers function
def lucas(n):
###Returns the lucas numbers based off a user defined number
	global _lucas
	if n == 2:
		return 2
    elif n == 1:
		return 1
    else:
		return lucas(n-1)+lucas(n-2)

def sum_series(n, first=0, second=1):
    if n == first:
        return first
    elif n == second:
        return second
    else:
        return sum_series(n-first)+sum_series(n-second)

if __name__ == "__main__":
