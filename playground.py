def add(*arg):
    total = 0
    for n in arg:
        total += n
    return total


print(add(1, 2, 1, 1, 1))
