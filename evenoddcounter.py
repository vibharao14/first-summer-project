
def checkEven(num):
	global sum
	if num % 2 == 0:
		return "even"
	else:
		return "odd"

num = int(input("Enter a number: "))
sum = 0
for i in range (num+1):
	print(f"{i} is {checkEven(i)}")
	if i % 2 == 0:
		sum += i
	

print(f"Sum of evens is {sum}")
