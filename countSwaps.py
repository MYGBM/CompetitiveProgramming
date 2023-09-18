#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swaps=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                swaps+=1
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f"Last Element: {a[len(a)-1]}")
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
