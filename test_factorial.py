import math
import pytest

# Function to test
def factorial(n):
    return math.factorial(n)

# Test cases
@pytest.mark.parametrize("n, expected", [
    (0, 1),    # 0! = 1
    (1, 1),    # 1! = 1
    (5, 120),  # 5! = 120
    (7, 5040), # 7! = 5040
    (10, 3628800),  # 10! = 3628800
])
def test_factorial(n, expected):
    assert factorial(n) == expected
