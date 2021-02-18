# Python use of inner functions
#code is taken from https://realpython.com/inner-functions-what-are-they-good-for/

def factorial(number):
    # Validate input
    if not isinstance(number,int):
        raise TypeError("Number must be integer")
    if number < 0:
        raise ValueError("Number must  number must be ")
    # Calculate the factorial of number
    def inner_factorial(number):
        if number <=1:
            return number
        return number*inner_factorial(number-1)
    return inner_factorial(number)

print(factorial(4))


