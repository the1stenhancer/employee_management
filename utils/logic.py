# This python module contains logic for the program
from data.models import Enterprise


def home_header():
    print()
    print(" "*20, "*"*45)
    print(" "*20, "*", " "*41, "*")
    print(" "*20, "*", " "*10, "EMPLOYEE MANAGEMENT", " "*10, "*")
    print(" "*20, "*", " "*41, "*")
    print(" "*20, "*"*45)
    print()
    print("Welcome! Choose one of the options below to proceed")
    print()
    print("[0]: Exit program")
    print("[1]: Hire employee")
    print("[2]: Display employees")
    print("[3]: Mute employee")
    print("[4]: Dismiss employee")
    print()


def enterprise_instance(name: str) -> Enterprise:
    return Enterprise(name=name)


def hire_employee(enterprise: Enterprise) -> None:
    enterprise.hire_employee()


def display_employees(enterprise: Enterprise) -> None:
    enterprise.display_employees()
