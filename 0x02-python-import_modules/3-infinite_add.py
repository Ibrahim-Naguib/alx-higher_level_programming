#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    result = 0
    for i in range(args):
        result += int(sys.argv[i + 1])
    print(result)
