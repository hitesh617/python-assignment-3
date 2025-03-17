# Calculate Factorial Using a Function 

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

result = int(input("Enter a number: ")) 

print("Factorial of", result, "is:", factorial(result))   