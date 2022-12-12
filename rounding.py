#!/usr/bin/env python3
# Created by: Minab Berhane
# Created on: Dec. 12, 2022
# This program asks the user to enter a decimal
# number and the number of decimal places they would
# like to round. It then rounds the number to the
# number of specified decimal places.


# this function rounds the user number to the
# correct amount of decimal places
def round_decimal(num_array, dec_places):
    # process for rounding number
    num_array[0] = num_array[0] * (10 ** dec_places)
    num_array[0] += 0.5
    num_array[0] = int(num_array[0])
    num_array[0] = num_array[0] / (10 ** dec_places)


# gets input from user, catches invalid data,
# and displays results to console
def main():

    # display opening message
    print("This program rounds a decimal to the number of "
          "decimal places entered.")
    print("")

    # declaring lists
    num_user = []

    # get decimal number from user
    dec_num_string = input("Enter a decimal number: ")

    try:
        # convert string to float
        dec_num_float = float(dec_num_string)

        # adds item to list
        num_user.append(dec_num_float)

        # gets number of decimal places from user
        dec_places_string = input("Enter the number of decimal places: ")

        try:
            # convert string to int
            dec_places_int = int(dec_places_string)

            # checks if number is negative
            if dec_places_int < 0:
                print("{} is not a positive integer." .format(dec_places_int))
            else:

                # calls function to round numbers
                round_decimal(num_user, dec_places_int)

                print("{} rounded to {} decimals is {}"
                      .format(dec_num_float, dec_places_int, num_user[0]))

        # catch invalid strings
        except Exception:
            print("Invalid input!")

    # catch invalid data
    except Exception:
        print("{} is not a decimal number" .format(dec_num_string))


if __name__ == "__main__":
    main()