# This is python module contains the classes necessary for the proper functioning of the program


# global variable representing hourly salary for temporal employees:
hourly_salary: float = 2500

# global variable representing commission on sales for seller employees:
commission: float = 0.1

# global variable representing monthly bonus for married employees that have kids
mb: float = 50000

# global variable representing fixed salary for permanent employees
fs: float = 300000


class Enterprise():

    def __init__(self, name: str):
        self.name: str = name
        self.employees: dict[str | object] = {}
    
    
    def hire_employee(self) -> None:
        # This method enables the enterprise to hire any category of employee
        print()

        name: str = input("Enter employee name [e.g. John Doe]: ")
        status: str = input("Enter employee status [permanent | temporal | seller]: ")

        if status == "permanent":
            fixed_salary: float = float(input(f"Enter fixed salary for {name} [e.g. 200000]: "))
            try:
                married: str = input(f"Is {name} married [yes | no]: ")
                if married.lower() == "yes":
                    try:
                        num_children: int = int(input(f"How many children does {name} have [e.g. 1]: "))
                        monthly_bonus: float = float(input(f"Enter monthly bonus for {name} [e.g. 50000]: "))
                        new_perm_emp: PermanentEmployee = PermanentEmployee(
                            name=name, 
                            status=status,
                            fixed_salary=fixed_salary,
                            monthly_bonus=monthly_bonus,
                            marital_status="married",
                            num_children=num_children
                        )
                        
                        # add new permanent employee to enterprise employee dictionary
                        self.employees[name] = new_perm_emp
                        print(f"{name} is officially a {status} employee for {self.name}")
                    except ValueError:
                        print("Error: number of children must be an integer greater than 1.")
                        print("Operation aborted.\n")
                else:
                    new_perm_emp: PermanentEmployee = PermanentEmployee(
                            name=name, 
                            status=status,
                            fixed_salary=fixed_salary,
                            marital_status="not married",
                    )
                    # add new permanent employee to enterprise employee dictionary
                    self.employees[name] = new_perm_emp
                    print(f"{name} is officially a {status} employee for {self.name}")
            except ValueError:
                print("Error: invalid input to marriage question.")
                print("Operation aborted.\n")
    
        elif status == "temporal":
            try:
                hours_worked: float = float(input(f"Hours worked by {name} [e.g. 60.5]: "))
                hourly_salary: float = float(input(f"Hourly salary for {name} [e.g. 2500]: "))
                new_temp_emp: TemporalEmployee = TemporalEmployee(
                    name=name,
                    status=status,
                    hours_worked=hours_worked,
                    hourly_salary=hourly_salary
                )
                # add temporal employee to enterprise employee dictionary
                self.employees[name] = new_temp_emp
                print(f"{name} is officially a {status} employee for {self.name}")
            except ValueError:
                print("Error: enter a valid amount.")
                print("Operation aborted.\n")
        
        elif status == "seller":
            try:
                hours_worked: float = float(input(f"Hours worked by {name} [e.g. 60.5]: "))
                hourly_salary: float = float(input(f"Hourly salary for {name} [e.g. 2500]: "))
                sold_volume: float = float(input(f"Sold volume for {name} [e.g. 500000]: "))
                commission: float = float(input(f"Commission for {name} [e.g. 0.1]: "))
                new_seller_emp: Seller = Seller(
                    name=name,
                    status=status,
                    hours_worked=hours_worked,
                    hourly_salary=hourly_salary,
                    sold_volume=sold_volume,
                    commission=commission
                )
                # add seller employee to enterprise employee dictionary
                self.employees[name] = new_seller_emp
                print(f"{name} is officially a {status} employee for {self.name}")
            except ValueError:
                print("Error: Invalid value for hourly salary or commission entered.")
                print("Operation aborted.\n")
    

    def display_employees(self):
        # This method prints out all the employees currently working for the enterprise with their details

        counter: int = 1

        if len(self.employees.keys()) < 1:
            print("\nThere are currently no employees in the enterprise.\n")
        else:
            for (key, value) in self.employees.items():
                print(f"[{counter}] {key}\n")
                print(f"Status: {value.status}")
                value.cumul_salary()
                if value.status == "permanent":
                    print(f"Marital status: {value.marital_status}")
                    print(f"Number of children: {value.num_children}")
                    print(f"Monthly bonus: {value.monthly_bonus}")
                    print(f"Fixed Salary: {value.fixed_salary}")
                    print(f"Days worked: {value.days_worked}")
                if value.status == "temporal":
                    print(f"Hourly salary: {value.hourly_salary}")
                    print(f"Hours worked: {value.hours_worked}")
                if value.status == "seller":
                    print(f"Sold volume: {value.sold_volume}")
                    print(f"Commission: {value.commission}")
                print(f"Cumulated salary: {value.cumulated}")
                print()
                print("-"*30)
                print()
                counter += 1
    

    def mute_employee(self, name: str, current_role: str, new_role: str) -> None:
        # check if new_role is an actual role in the enterprise
        if new_role in ("permanent", "temporal", "seller"):
            # check that name is a valid employee in enterprise
            if name in self.employees.keys():
                # collect employee instance from enterprise employees database
                employee: object = self.employees[name]
                # verify that employee status matches current_role
                if employee.status == current_role:
                    # check if current_role is equal to new_role
                    if current_role == new_role:
                        print(f"\n[Error]: Cannot mute {name} from {current_role} to {new_role}: they are the same.\n")
                    else:
                        # if current_role is permanent
                        if current_role == "permanent":
                            # if new_role is temporal
                            if new_role == "temporal":
                                hours_worked: float = employee.cumulated / hourly_salary
                                muted_employee: TemporalEmployee = TemporalEmployee(
                                    name=name,
                                    hours_worked=hours_worked
                                )
                                self.employees[name] = muted_employee
                                
                            elif new_role == "seller":
                                # if new_role is seller
                                sold_volume: float = employee.cumulated / commission
                                muted_employee: Seller = Seller(
                                    name=name,
                                    sold_volume=sold_volume
                                )
                                self.employees[name] = muted_employee

                        elif current_role == "temporal":
                            if new_role == "permanent":
                                # is the employee married and has kids?
                                marital_status: str = input(f"Is {name} married [ yes | no ]: ")
                                if marital_status.lower() == "yes":
                                    nc: int = int(input(f"Number of children [e.g. 1]: "))
                                    days_worked: float = (20 * employee.cumulated) / (fs + mb)
                                    muted_employee: PermanentEmployee = PermanentEmployee(
                                        name=name,
                                        days_worked=days_worked,
                                        marital_status="married",
                                        num_children=nc,
                                        monthly_bonus=mb
                                    )
                                    self.employees[name] = muted_employee
                                else:
                                    days_worked: float = (20 * employee.cumulated) / fs
                                    muted_employee: PermanentEmployee = PermanentEmployee(
                                        name=name,
                                        days_worked=days_worked
                                    )
                                    self.employees[name] = muted_employee
                                
                            elif new_role == "seller":
                                sold_volume: float = employee.cumulated / commission
                                muted_employee: Seller = Seller(
                                    name=name,
                                    sold_volume=sold_volume
                                )
                                self.employees[name] = muted_employee

                        elif current_role == "seller":
                            if new_role == "permanent":
                                # is the employee married and has kids?
                                marital_status: str = input(f"Is {name} married [ yes | no ]: ")
                                if marital_status.lower() == "yes":
                                    nc: int = int(input(f"Number of children [e.g. 1]: "))
                                    days_worked: float = (20 * employee.cumulated) / (fs + mb)
                                    muted_employee: PermanentEmployee = PermanentEmployee(
                                        name=name,
                                        days_worked=days_worked,
                                        marital_status="married",
                                        num_children=nc,
                                        monthly_bonus=mb
                                    )
                                    self.employees[name] = muted_employee
                                else:
                                    days_worked: float = (20 * employee.cumulated) / fs
                                    muted_employee: PermanentEmployee = PermanentEmployee(
                                        name=name,
                                        days_worked=days_worked
                                    )
                                    self.employees[name] = muted_employee
                            elif new_role == "temporal":
                                hours_worked: float = employee.cumulated / hourly_salary
                                muted_employee: TemporalEmployee = TemporalEmployee(
                                    name=name,
                                    hours_worked=hours_worked
                                )
                                self.employees[name] = muted_employee

                        print(f"\nSuccessfully muted {name} from a {current_role} to {new_role} employee.\n")
                else:
                    print(f"\n[Error]: {name} is a {employee.status} employee, not {current_role}.\n")
            else:
                print(f"\n[Error]: {name} is not an employee in this enterprise.\n")
        else:
            print(f"\n[Error]: '{new_role}' is not an employee category in this enterprise.\n")


    def dismiss_employee(self, name: str) -> None:
        try:
            if name not in self.employees.keys():
                raise KeyError
            else:
                self.employees.pop(name)
                print(f"\n{name} is no longer an employee in the enterprise.\n")
        except KeyError:
            print(f"\n{name} is not an employee of this enterprise.\n")
            


class Employee():
    
    def __init__(self, name: str, status: str):
        self.name: str = name
        self.status: str = status


class PermanentEmployee(Employee):

    def __init__(
        self,
        name: str,
        status: str = "permanent",
        days_worked: int = 0,
        fixed_salary: float = fs,
        num_children: int = 0,
        marital_status: str = "not married",
        monthly_bonus: float = 0.0,
    ):
        super().__init__(name, status)
        self.days_worked: int = days_worked
        self.fixed_salary: float = fixed_salary
        self.num_children: int = num_children
        self.marital_status: str = marital_status
        self.monthly_bonus: float = monthly_bonus
        self.cumulated: float = 0.0
    

    def cumul_salary(self) -> float:
        if self.marital_status == "married":
            salary: float = (self.days_worked * (self.fixed_salary + self.monthly_bonus)) / 20
        else:
            salary: float = (self.days_worked * self.fixed_salary) / 20
        self.cumulated += salary
        return self.cumulated


class TemporalEmployee(Employee):
    
    def __init__(
        self, 
        name: str, 
        status: str = "temporal", 
        hourly_salary: float = hourly_salary, 
        hours_worked: float = 0.0
    ):
        super().__init__(name, status)
        self.hourly_salary: float = hourly_salary
        self.hours_worked: float = hours_worked
        self.cumulated: float = 0.0
    

    def cumul_salary(self) -> float:
        salary: float = (self.hourly_salary * self.hours_worked)
        self.cumulated += salary
        return self.cumulated


class Seller(TemporalEmployee):

    def __init__(
        self, 
        name: str,
        status: str = "seller",
        hourly_salary: float = hourly_salary,
        hours_worked: float = 0.0,
        sold_volume: float = 0.0,
        commission: float = commission
    ):
        super().__init__(name, status, hourly_salary, hours_worked)
        self.sold_volume: float = sold_volume
        self.commission: float = commission
        self.cumulated: float = 0.0
    

    def cumul_salary(self):
        salary: float = (self.sold_volume * self.commission)
        self.cumulated += salary

