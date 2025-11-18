#!/usr/bin/python3

import sys

if __name__ == "__main__":

    sum = 0

    arg_count = len(sys.argv) - 1

    for i in range(1, len(sys.argv)):

        num = int(sys.argv[i])

        sum += num


    print(sum) 
