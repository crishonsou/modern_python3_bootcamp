import math
import os
import random
import re
import sys

##### Variables

#num_cicles = n
#initial_height = 1

def utopianTree(n):
    x = 0
    for i in range(n + 1):
        if i % 2:
            x *= 2
        else:
            x += 1
    return x

for i in range(int(input())):
    print(utopianTree(int(input())))
