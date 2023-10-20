# write function f(x) taht returns x**3 + 8

def f(x):
	return x**3 + 8

# now define and start main function 

def main():
	x = 9
	result_of_function = f(x)

	print(f"The result of f({x}) is {result_of_function}")

	if result_of_function > 27:
		print("YAY!")

if __name__ == "__main__":
	main()