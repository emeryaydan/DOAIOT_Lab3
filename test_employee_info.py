import pytest
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept, employee_data

def test_get_employees_by_age_range():
    result = get_employees_by_age_range(25, 35)
    assert len(result) == 4
    assert all(25 < employee['age'] < 35 for employee in result)

def test_calculate_average_salary():
    average_salary = calculate_average_salary()
    expected_average = sum(employee['salary'] for employee in employee_data) / len(employee_data)
    assert average_salary == round(expected_average, 2)

def test_get_employees_by_dept():
    result = get_employees_by_dept("Sales")
    assert len(result) == 2
    assert all(employee['department'] == "Sales" for employee in result)