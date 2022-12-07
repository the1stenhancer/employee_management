# This is the entry point to the python program
import sys
from utils.logic import home_header


if __name__ == "__main__":
    home_header()

    try:
        choice: int = int(input("Your choice: "))
        if choice == 0:
            print("\nThank you for using the program.\nGoodbye!\n")
            sys.exit()
        elif choice == 1:
            pass
        else:
            print("Enter a valid choice next time.")
    except TypeError:
        print("Error: you did not enter a valid number.")

    print()
