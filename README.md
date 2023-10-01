# pairs-sum

O(n) python solution using set for Mach Eight technical challenge: write a function that finds pairs of integers from a list that
sum to a given value. The function will take as input the list of numbers as well as the target sum. It can be assumed all values are integers and there aren't duplicate values.

## Table of Contents
- [Files](#files)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Files

- `pairs_sum.py`: File containing the O(n) solution for the problem, finds pairs of numbers in an array that sum up to a given target value

- `main.py`: This is the main Python script of the project. Calls the pairs_sum function and provides simple input, error handling, and result printing.

- `test_pairs_sum.py`: Contains unittest unit tests for the `pairs_sum` function. It ensures that the algorithm works correctly and that edge cases are handled.

## Usage

To use pairs_sum, follow these steps:

1. Run the main.py script using Python 3:

```bash
python3 main.py <comma-separated-array> <target-sum>
```

2. Replace <comma-separated-array> with your input array (e.g., 1,9,5,0,20,-4,12,16,7) and <target-sum> with your desired target sum (e.g., 12).

Example:

```bash
python3 main.py 1,9,5,0,20,-4,12,16,7 12
```
Results:
- 12, 0
- 16, -4
- 7, 5

## Running Tests

You can run the unit tests for pairs_sum to ensure its correctness. Navigate to the project directory and run the following command:

```bash
python3 -m unittest test_pairs_sum
```
