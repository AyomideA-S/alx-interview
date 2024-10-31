# 0x0A. Prime Game

## Description

Maria and Ben take turns picking prime numbers from a set of integers from 1 to `n`. Picking a prime removes it and its multiples. The player unable to make a move loses. Given `x` rounds with different values of `n`, determine who wins each game assuming both play optimally. Maria always starts first.

## Prototype

```python
def isWinner(x, nums):
```

- `x`: the number of rounds
- `nums`: an array of integers representing `n` for each round

**Returns**: The name of the player that won the most rounds. If the winner cannot be determined, return `None`.

## Constraints

- You can assume `n` and `x` will not be larger than 10000.
- You cannot import any packages in this task.

## Example

```python
x = 3
nums = [4, 5, 1]
```

### First Round: `n = 4`

- Maria picks 2 and removes 2, 4, leaving 1, 3.
- Ben picks 3 and removes 3, leaving 1.
- Ben wins because there are no prime numbers left for Maria to choose.

### Second Round: `n = 5`

- Maria picks 2 and removes 2, 4, leaving 1, 3, 5.
- Ben picks 3 and removes 3, leaving 1, 5.
- Maria picks 5 and removes 5, leaving 1.
- Maria wins because there are no prime numbers left for Ben to choose.

### Third Round: `n = 1`

- Ben wins because there are no prime numbers for Maria to choose.

**Result**: Ben has the most wins.

## Usage Example

```bash
carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
carrie@ubuntu:~/0x0A-primegame$
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
