# This python module contains logic for the program
from data.models import Enterprise


# headers

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


def display_header():
    print()

    print(" "*27, "********** Employees **********")
    print()


def mute_header():
    print()

    print(" "*27, "********** Mute Employee **********")
    print()


# Helper functions 

def enterprise_instance(name: str) -> Enterprise:
    return Enterprise(name=name)


def hire_employee(enterprise: Enterprise) -> None:
    enterprise.hire_employee()


def display_employees(enterprise: Enterprise) -> None:
    display_header()
    enterprise.display_employees()


def mute_employee(enterprise: Enterprise) -> None:
    mute_header()
    name: str = input("Enter employee name [e.g. John Doe]: ")
    current_role: str = input("Enter current role [e.g. permanent]: ")
    new_role: str = input("Enter new role [e.g. temporal]: ")
    enterprise.mute_employee(name=name, current_role=current_role, new_role=new_role)
    pass
