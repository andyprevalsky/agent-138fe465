"""Compute and print the Collatz sequence starting from 27.

Rule for each step:
  - if n is even: n = n // 2
  - if n is odd:  n = 3 * n + 1

Every number in the sequence is printed, one per line, from the starting
value through the final 1, followed by the total number of steps
(transitions) taken to reach 1.
"""

START = 27


def collatz_sequence(start: int) -> tuple[list[int], int]:
    """Return (sequence, steps) for the Collatz sequence from start to 1.

    The sequence includes both the starting value and the final 1. Steps is
    counted independently, once per transition applied.
    """
    if start < 1:
        raise ValueError("start must be a positive integer")
    sequence = [start]
    steps = 0
    n = start
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
        steps += 1
    return sequence, steps


def main() -> None:
    sequence, steps = collatz_sequence(START)

    for n in sequence:
        print(n)

    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()
