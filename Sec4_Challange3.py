def f(x,y,z=1,m=2):
    print(x,y,z,m)
    return x + y + z + m

a = input("Type a number:")
b = input("type another:")

try:
    a = int(a)
    b = int(b)
    print(f(a,b))
except ValueError:
    print("You have to type in numbers.")
