list1 = [3, 7]

while True:
    x = input("Please type in a digit: ")
    y = False
    if ( x == "q"):
        break
    try:
        x = int(x)
    except ValueError:
        print("please type a digit or q to quit.")
    for i in list1:
        if (x == int(i)):
            y = True
    if y == True:
        print("matched")
    else:
        print("not mached")
