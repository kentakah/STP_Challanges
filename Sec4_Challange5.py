def func1(str1):
    """
    Returns input string value converted to float value.
    :param str1: string
    :return float, str1 converted from string to float.
    """
    return float(str1)

a = input("Type in a string:")

try:
    print(a)
    b = func1(a)
    print(b)
except ValueError:
    print("Can't convert to flaot?")
