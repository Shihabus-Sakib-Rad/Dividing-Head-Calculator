# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:16:45 2020

@author: shiha
"""
import itertools
import math

def get_gear_set_ratio(A,N,ratio=40):
    return (A-N)*(ratio/A)

def find_gear_set(gear_ratio, gear_set):
    all_perm = itertools.permutations(gear_set, 2)
    result=[]
    for gear_pair in all_perm:
        spindle, worm= gear_pair
        if math.isclose(gear_ratio, spindle/worm):
            result.append((spindle, worm))
            
    return result
            
def main():
    gear_set= [24, 28, 32, 40, 44, 48, 56, 64, 72, 86]
    r= get_gear_set_ratio(56, 57)
    results = find_gear_set(abs(r), gear_set)
    
    for result in results:
        print("Spindle {} -- Worm {}".format(result[0], result[1]))
        
if __name__ == "__main__":
    main()