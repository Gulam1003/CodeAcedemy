from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    employee_id: int
    name: str
    age: int
    salary: int
    department: "Department"

@dataclass
class Department:
    department_id: int
    name: str
    employees: List[Employee]

    def average_salary(self):
        total_salaries = sum([employee.salary for employee in self.employees])
        if len(self.employees) == 0:
            return 0
        return total_salaries / len(self.employees)

@dataclass
class EmployeeManagement:
    departments: List[Department]

    def total_salary(self):
        total_salaries_departments = 0
        for department in self.departments:
            total_salaries = sum([employee.salary for employee in department.employees])
            total_salaries_departments += total_salaries
        return total_salaries_departments

    def get_employees_in_age_range(self, min_age, max_age):
        age_range_employees = []
        for department in self.departments:
            for employee in department.employees:
                if min_age <= employee.age <= max_age:
                    age_range_employees.append(employee)
        return age_range_employees

    def sort_employees_by_salary(self):
        employees_by_salary = []
        for department in self.departments:
            employees_by_salary.extend(department.employees)
        return sorted(employees_by_salary, key=lambda x: x.salary, reverse=True)

    def filter_employees_by_department(self, department_name: str):
        for department in self.departments:
            if department.name == department_name:
                return department.employees

"""
Explanation:
EmployeeManagement Class: Manages multiple departments and employees.
- total_salary: Calculates and returns the total salary of all employees in the organization.
- get_employees_in_age_range: Returns a list of employees within a specified age range.
- sort_employees_by_salary: Returns a sorted list of employees by their salary in descending order.
- filter_employees_by_department: Returns a list of employees in a specified department.
"""

# Instantiate Employee objects
emp1 = Employee(1, "Tom", 25, 1500, None)
emp2 = Employee(2, "Tim", 27, 1855, None)
emp3 = Employee(3, "John", 66, 2000, None)
emp4 = Employee(4, "Sam", 55, 2500, None)

# Instantiate Department objects
dep1 = Department(11, "IT", [emp1, emp2])
dep2 = Department(12, "Finance", [emp3, emp4])

# Instantiate EmployeeManagement object
empmng = EmployeeManagement([dep1, dep2])

# Testing methods
print(empmng.get_employees_in_age_range(15, 28))
print(empmng.sort_employees_by_salary())
print(empmng.filter_employees_by_department("IT"))
print(dep1.average_salary())
print(empmng.total_salary())
