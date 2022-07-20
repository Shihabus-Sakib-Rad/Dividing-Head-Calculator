# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:25:54 2020

@author: shiha
"""
import itertools
import math

def find_compound_index(N, plate, ratio=40):
    result=[]
    all_combin= itertools.combinations(plate, 2)
    
    for N1, N2 in all_combin:
        n=(ratio * N1 * N2)/(N * (N2-N1))
        if math.isclose(n, round(n)):
            result.append((N1, N2, n))
                
    return result

def print_result(cw_comp, n1, N1, ccw_comp, n2, N2):
    if cw_comp!=0 or n1!=0:
        print("Crank", end=" ")
    if cw_comp>0:
        print("{} complete turn".format(cw_comp), end=" ")
    if cw_comp>0 and n1!=0:
        print("and", end=" ")
    if n1!=0:
        print("{} holes in {} holes circle".format(n1, N1), end=" ")
    if cw_comp!=0 or n1!=0:
        print("in CW direction", end=" ")
        
    if ccw_comp!=0 or n2!=0:
        print("---- plate", end=" ")
    if ccw_comp>0:
        print("{} complete turn".format(ccw_comp), end=" ")
    if ccw_comp>0 and n2!=0:
        print("and", end=" ")
    if n2!=0:
        print("{} holes in {} holes circle".format(n2, N2), end=" ")
    if ccw_comp!=0 or n2!=0:
        print("in CCW")
        
    print()
    

def interpret_result(t):
    N1, N2, n=t
    cw_comp , ccw_comp = 0, 0
    if n>N1: cw_comp = math.floor(n/N1)
    if n>N2: ccw_comp = math.floor(n/N2)
    common = min(cw_comp, ccw_comp)
    cw_comp=cw_comp-common
    ccw_comp=ccw_comp-common
    n1=n%N1
    n2=n%N2
    
    return (cw_comp, n1, N1, ccw_comp, n2, N2)

    

def main():
    plate1 = [15,16,17,18,19,20]
    plate2 = [21,23,27,29,31,33]
    plate3 = [37,39,41,43,47,49]
    
    plates=[plate1, plate2, plate3]
    
    for plate_no, plate in enumerate(plates):   
        results=find_compound_index(69, plate)
        if len(results)!=0:
            print("----Plate No {}----".format(plate_no+1))
        for result in results:
            print(result, end="-- ")
            print_result(*interpret_result(result))
        
    print("finished")
    
if __name__ == "__main__":
    main()
        
    

