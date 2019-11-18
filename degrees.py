#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : November 2019
# This function that will convert the Celsuius to Fahrenheit


def degree_in_celsius():
    # this function that will convert the Celsuius to Fahrenheit

    # input
    Tc = int(input("Enter a degree in Celsius: "))
    Tf = (9/5)*Tc+32
    print(Tf)


def main():
    # this function just calls other functions

    # call functions
    degree_in_celsius()


if __name__ == "__main__":
    main()
