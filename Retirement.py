import calcRetirement
from datetime import *


def main():
    print("Social Security Full Retirement Age Calculator")
    birthYear = year_input()
    birthMonth = month_input()
    retireAge, retireMonth = calcRetirement.retirement(birthYear)
    retirementYear, retirementMonth = calcRetirement.calculate_retirement_date(birthYear, birthMonth, retireAge,
                                                                               retireMonth)
    print("Your retirement age is", retireAge, "and", retireMonth, "months.\nThis will be in", retirementMonth, "of",
          retirementYear, "\n")


def year_input():
    currentYear = int(datetime.now().year)
    while True:
        try:
            year = int(float(input("Enter the year of birth or <Enter> to exit: ")))
            while year not in range(1900, currentYear + 1):
                print("Invalid input. Year must be in between 1900 and up to current year")
                year = int(float(input("Enter the year of birth or <Enter> to exit: ")))
        except ValueError:  # Hitting Enter key to exit program.
            print("Incorrect input. Enter a number")
            continue

        return year


def month_input():
    global birthMonth
    while True:
        try:
            birthMonth = int(float(input("Enter the month of birth (as a number): ")))
            while birthMonth not in range(1, 13):
                print("Invalid input. Month must be between 1 and 12.")
                birthMonth = int(float(input("Enter the month of birth (as a number): ")))
        except ValueError:
            print("Incorrect input. Enter a number")
            continue

        return birthMonth




if __name__ == "__main__":
    main()
