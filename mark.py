#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Dec 2022
# This program calculates the average mark


def finds_the_average(marks):
    # This function finds the average

    total = 0

    for element in marks:
        total += element

    average = total / len(marks)

    return average


def main():
    # This function makes the list

    marks = []
    temp_int = None

    # Input
    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")

    while True:
        try:
            temp_number = input("What is your mark (as %): ")
            temp_int = int(temp_number)
            if temp_int <= 100 and temp_int >= 0:
                marks.append(temp_int)
            elif temp_int == -1:
                average = finds_the_average(marks)
                print("\nThe average is {0}%".format(average))
                break
            temp_int = int(temp_number)
            marks.append(temp_int)
        except Exception:
            print("Invalid Input")
            continue

    print("\nDone.")


if __name__ == "__main__":
    main()
