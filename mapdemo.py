one_to_4 = range(1, 5)


def times2(x): return x * 5


print(list(map(times2, one_to_4)))


# Filter
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# print(reduce((lambda x, y: x + y), range(1, 6)))
