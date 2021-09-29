
def factorial(num):
    prod = num
    for i in reversed(range(1, num + 1)):
        print(f'{prod} TIMES {i} EQUALS {prod * i}')
        prod *= i
    return prod

print(factorial(10))