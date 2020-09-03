def fizzbuzz(a):
    if a % 3 == 0 and a % 5 != 0:
        return "Fizz"
    elif a % 5 == 0 and a % 3 != 0:
        return "Buzz"
    elif a % 3 == 0 and a % 5 == 0:
        return "FizzBuzz"
    else:
        return a



# print(fizzbuzz(3))
# print(fizzbuzz(5))
# print(fizzbuzz(15))
# print(fizzbuzz(4))