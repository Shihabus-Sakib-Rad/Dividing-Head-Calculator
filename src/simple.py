# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:53:03 2020

@author: shiha
"""
import math
from fractions import Fraction


def find_simple_index(N, plate, ratio=40):
    crank_turn = Fraction(ratio, N)
    results = []
    for row in plate:
        temp = row / crank_turn.denominator
        if math.isclose(temp, round(temp)):
            holes = temp * crank_turn.numerator
            results.append((row, holes))
    return results


def interpret_result_simple(result: tuple):
    row, holes = result
    cw_comp = 0
    extra_holes = holes
    if holes > row:
        cw_comp = math.floor(holes/row)
        extra_holes = holes % row

    return (cw_comp, extra_holes, row)


def main():
    plate1 = [15, 16, 17, 18, 19, 20]
    plate2 = [21, 23, 27, 29, 31, 33]
    plate3 = [37, 39, 41, 43, 47, 49]
    plates = [plate1, plate2, plate3]

    for plate_no, plate in enumerate(plates):
        results = find_simple_index(30, plate)
        if len(results) != 0:
            print("----Plate No {}----".format(plate_no+1))
        for result in results:
            print(interpret_result_simple(result))

    print("finished")


if __name__ == "__main__":
    main()
