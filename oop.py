class MyClass:
    pass


class MyError(Exception):
    pass


c = MyClass()
print(dir(c))

raise MyError()
