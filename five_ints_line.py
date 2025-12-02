#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Dec 1st, 2025
# this program prints the integers from 1000 to 2000,
# outputting five integers per line with each separated by a space.


def main():
    count = 0
    for i in range(1000, 2001):
        print(i, end=" ")
        count += 1
        if count % 5 == 0:
            print()  # print a new line every 5 numbers


if __name__ == "__main__":
    main()
