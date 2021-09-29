
def curzon(num):
    return not (2 ** num + 1) % (2 * num + 1)

print(curzon(5))
print(curzon(10))