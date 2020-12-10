#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nbr = len(sys.argv) - 1
    if nbr == 1:
        print("1 argument:")
    elif nbr == 0:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(nbr))
    for i in range(1, nbr + 1):
        print("{:d}: {:s}".format(i, (sys.argv[i])))
