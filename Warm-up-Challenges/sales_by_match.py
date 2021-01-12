import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors_dict = dict()
    matching = 0
    for x in range(0,n):
        if ar[x] not in colors_dict:
            colors_dict[ar[x]] = 1
        else:
            colors_dict[ar[x]] += 1

        if colors_dict.get(ar[x])%2==0:
            matching +=1
    return matching


if __name__ == '__main__':
    sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])


