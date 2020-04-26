def func1(v1, v2):
    print(v1 is v2)

try:
    while True:
        x = input("input first value: ")
        y = input("input another value: ")
        func1(x, y)
except KeyboardInterrupt:
    print("done..")
