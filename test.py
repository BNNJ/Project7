#!/usr/bin/env python3

# Input:
# Values (stored in list `v`)
# Weights (stored in list `w`)
# Total number of distinct items `n`
# Knapsack capacity `W`
def knapsack(v, w, W):
 
    # `T[i][j]` stores the maximum value of knapsack having weight less
    # than equal to `j` with only first `i` items considered.
    T = [[0 for x in range(W + 1)] for y in range(len(v) + 1)]
 
    # do for i'th item
    for i in range(1, len(v) + 1):
 
        # consider all weights from 0 to maximum capacity `W`
        for j in range(W + 1):
 
            # don't include the i'th element if `j-w[i-1]` is negative
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find the maximum value we get by excluding or including the i'th item
                T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i - 1]] + v[i - 1])
 
    # return maximum value
    return T[len(v)][W]
 
 
if __name__ == '__main__':
 
    # input: a set of items, each with a weight and a value
    v = [20, 5, 10, 40, 15, 25]
    w = [1.3, 2.1, 3.5, 8.2, 7.6, 4.2]
 
    # knapsack capacity
    W = 10
 
    print("Knapsack value is", knapsack(v, w, W))