# 0x05. N Queens

## Description

The N Queens puzzle involves placing N non-attacking queens on an N×N chessboard. This program solves the N Queens problem by printing all possible solutions.

## Usage

```bash
nqueens N
```

- **Arguments**:
  - `N`: An integer greater than or equal to 4.

- **Error Handling**:
  - If the number of arguments is incorrect, the program prints:

    ```txt
    Usage: nqueens N
    ```

    and exits with status 1.
- If `N` is not an integer, it prints:

    ```txt
    N must be a number
    ```

    and exits with status 1.
- If `N` is less than 4, it prints:

    ```txt
    N must be at least 4
    ```

    and exits with status 1.

- **Output**:
  - Prints every possible solution, one per line, in the following format:

    ```python
    [[column_0, row_0], [column_1, row_1], ..., [column_N-1, row_N-1]]
    ```

  - Solutions are not required to be in any specific order.

- **Restrictions**:
  - Only the `sys` module is allowed.

## Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
