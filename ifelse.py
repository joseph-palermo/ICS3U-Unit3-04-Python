#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program sees if an integer is positive, negative, or zero


def main():
    # This function sees if an integer is positive, negative, or zero

    # input
    number = int(input("Write in an integer: "))
    print("")

    # process
    if number == 0:
        print("It equals zero!")
    elif number > 0:
        print("It is positive!")
    elif number < 0:
        print("It is negative!")
    else:
        print("Uhhhhhh what")


if __name__ == "__main__":
    main()
