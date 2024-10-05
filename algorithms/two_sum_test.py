import pytest
from .two_sum import Solution

@pytest.fixture
def solution():
    return Solution()

def test_two_sum_example1(solution):
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_example2(solution):
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]

def test_two_sum_example3(solution):
    assert solution.twoSum([3, 3], 6) == [0, 1]

def test_two_sum_no_solution(solution):
    assert solution.twoSum([1, 2, 3], 7) == []

def test_two_sum_multiple_solutions(solution):
    assert solution.twoSum([1, 2, 3, 4, 4], 8) == [3, 4]

def test_two_sum_negative_numbers(solution):
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
