# This is python module contains the classes necessary for the proper functioning of the program


class Enterprise():

    def __init__(self, name: str, employees: dict[str | object]):
        self.name: str = name
        self.employees: dict[str | object] = employees
    
    
    def hire_employee(self) -> None:
        # This method enables the enterprise to hire any category of employee
        pass


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
        fixed_salary: float = 500000.0,
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
        salary: float = (self.days_worked * (self.fixed_salary + self.monthly_bonus)) / 20
        self.cumulated += salary
        return self.cumulated


class TemporalEmployee(Employee):
    
    def __init__(
        self, 
        name: str, 
        status: str = "temporal", 
        hourly_salary: float = 2500, 
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
        status: str = "temporal",
        hourly_salary: float = 2500,
        hours_worked: float = 0.0,
        sold_volume: float = 0.0,
        commission: float = 0.1
    ):
        super().__init__(name, status, hourly_salary, hours_worked)
        self.sold_volume: float = sold_volume
        self.commission: float = commission
        self.cumulated: float = 0.0
    

    def cumul_salary(self):
        salary: float = super().cumul_salary() + (self.sold_volume * self.commission)
        self.cumulated += salary

