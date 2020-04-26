def func1(x):
    return x / 2

def func2(y):
    return y * 4

a = input("Type a number:")

try:
    a = int(a)
    b = func1(a)
    print(b)
except ValueError:
    print("You have to type in a number")

try:
    print(func2(b))
except ValueError:
    print("You have to type in a number")
