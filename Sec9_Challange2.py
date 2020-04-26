x = input("What is your favorite song?: ")

with open("fave_song.txt", "w") as f1:
    f1.write(x)
