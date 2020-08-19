#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n -= 1
    n3 = n//3
    n5 = n//5
    n15 = n//15
    sums = (3 * (n3)*(n3+1)//2) + (5 * (n5)*(n5+1)//2) - (15 * (n15)*(n15+1)//2)
    print(sums)
