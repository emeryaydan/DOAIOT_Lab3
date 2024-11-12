import pytest
from price_info import total_cost_shopping, cost_of_fruits, price_list, quantity_list

def test_total_cost_shopping(capsys):
    total_cost_shopping()
    captured = capsys.readouterr()
    expected_total = sum(price_list[fruit] * quantity_list[fruit] for fruit in price_list if fruit in quantity_list)
    assert f"total cost =  {expected_total}" in captured.out

def test_cost_of_fruits(capsys):
    cost_of_fruits('apple', 10)
    captured = capsys.readouterr()
    expected_cost = 10 * price_list['apple']
    assert f"cost of 10 apple = {expected_cost}" in captured.out

def test_cost_of_fruits_invalid_fruit(capsys):
    cost_of_fruits('banana', 5)
    captured = capsys.readouterr()
    assert "cost of  5 banana = " not in captured.out