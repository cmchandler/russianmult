#!/usr/bin/env python3
import math

"""
Demo for "russian multiplication"
cc 02/04/20
"""

while True:
    try:
        first = int(input("Please input first number: "))
        second = int(input("Please input second number: "))
    except ValueError:
        print("Please input valid integers.")
        continue
    else:
        break

x = origfirst = first
y = origsecond = second

board = []

while x > 0:
    board.append((x, y, x % 2 == 0))
    x = math.floor(x / 2)
    y = y * 2


print("\nResults before removing evens:")
print("\nFirst\t\tSecond")
print("-----\t\t------")
for first, second, even in board:
    print(f"{first}\t\t{second}")
input("\nPress enter to continue...")


print("\nAfter removing evens:")
print("\nFirst\t\tSecond")
print("-----\t\t------")
for first, second, even in board:
    if not even:
        print(f"{first}\t\t{second}")

input("\nPress enter to continue...")

print(f"\n{origfirst} * {origsecond} = {origfirst * origsecond}")

countme = []
for first, second, even in board:
    if not even:
        countme.append(second)

for num in countme:
    print(f"{num}", end='')
    if not num == countme[-1]:
        print(" + ", end='')

print(f" = {sum(countme)}\n")
