
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2


if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (division by zero)"


print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
