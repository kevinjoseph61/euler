#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    curr, prev, sums=2, 0, 0
    while curr<n:
        sums, curr, prev = sums + curr, 4 * curr + prev, curr
    print(sums)
