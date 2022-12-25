# This is the entry point to the python program
import sys
from utils.logic import *
from data.models import Enterprise


if __name__ == "__main__":

    home_header()

    # creating Enterprise instance at startup
    enterprise: Enterprise = enterprise_instance(name="Jeff Inc.")

    try:
        
        while True:

            choice: int = int(input("Your choice: "))

            if choice == 0:
                print("\nThank you for using the program.\nGoodbye!\n")
                sys.exit()

            elif choice == 1:
                hire_employee(enterprise=enterprise)
                home_header()
                
            elif choice == 2:
                display_employees(enterprise=enterprise)
                home_header()

            elif choice == 3:
                mute_employee(enterprise=enterprise)
                home_header()
                
            elif choice == 4:
                dismiss_employee(enterprise=enterprise)
                home_header()
                
            else:
                print("\nEnter a valid choice (0, 1, 2, 3 or 4) next time.\n")

    except ValueError:
        print("\nError: you did not enter a valid number (0, 1, 2, 3 or 4).\n")

    print()
