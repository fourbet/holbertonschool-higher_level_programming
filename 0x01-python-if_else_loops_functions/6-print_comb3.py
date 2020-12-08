#!/usr/bin/python3
for i in range(0, 100):
    dizaine = i // 10
    unite = i % 10
    if (unite > dizaine):
        if (i == 1):
            print("{:02d}".format(i), end="")
        else:
            print(", {:02d}".format(i), end="")
print()
