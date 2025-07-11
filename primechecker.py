
def is_prime(n):
	prime = True
	for j in range (2, n):
		if n % j == 0:
			prime = False
			print(f"{num} is composite")
			return prime
	print(f"{num} is prime")
	return prime

num = int(input("Enter a number: "))

is_prime(num)
