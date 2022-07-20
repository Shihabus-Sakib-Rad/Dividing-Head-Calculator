# Dividing-Head-Calculator
A program for Dividing Head used in Milling Operations to find the required index-plate, holes-circle and calculate the crank movement for simple &amp; compound indexing and also to find the suitable gear set for differential indexing.

Check out my other open-source programs for Mechanical Enginneers [here](https://github.com/Shihabus-Sakib-Rad)

Default Index-plate: **Brown and Sharp**
- Plate 1 : 15, 16, 17, 18, 19, 20
- Plate 2 : 21, 23, 27, 29, 31, 33
- Plate 3 : 35, 37, 39, 41, 43, 47, 49

You can also add other custom plates.

Default change gears: 24, 28, 32, 40, 44, 48, 56, 64, 72, 86

## Usages

### Example 1: Calculate crank movement for dividing the circumference of gear blank into 30 identical parts

Set the first argument of *find_simple_index()* to 30 in `simple.py file > main() function`.
```python
results = find_simple_index(30, plate)
```
Run the program. The program will output the following:
```
----Plate No 1----
(1, 5.0, 15)
(1, 6.0, 18)
----Plate No 2----
(1, 7.0, 21)
(1, 9.0, 27)
(1, 11.0, 33)
----Plate No 3----
(1, 13.0, 39)
finished
```

**Interpretation of Result:**
- If Plate 1 is selected, then rotate indexing crank by 1 complete turn and 5 holes in 15 holes-circle. 
- If Plate 2 is selected, then rotate indexing crank by 1 complete turn and 7 holes in 21 holes-circle.
- Similar logic applies to other results.

### Example 2: Make 69 divisions of workpiece circumference by compound indexing method.
Set the first argument of  *find_compound_index()* to 69 in `compound.py file > main() function`.
```python
results=find_compound_index(69, plate)
```
Run the program. The program will output the following:
```
----Plate No 2----
(21, 23, 140.0)-- Crank 14.0 holes in 21 holes circle in CW direction ---- plate 2.0 holes in 23 holes circle in CCW

(23, 27, 90.0)-- Crank 21.0 holes in 23 holes circle in CW direction ---- plate 9.0 holes in 27 holes circle in CCW

(23, 33, 44.0)-- Crank 21.0 holes in 23 holes circle in CW direction ---- plate 11.0 holes in 33 holes circle in CCW

finished
```
**Interpretation of Result:**
- Using plate 2, the indexing crank should be moved by 21 holes-circle in forward direction and then crank along with the plate are moved by 11 holes in 33 hole-circle is reversed (backward) direction.


### Example 3: Find change gears required for 57 divisions.
Set the first and second argument of *get_gear_set_ratio()* to 56, 57 in `differential.py file > main() function`. Make necessary change to the supplied gear set.
```python
gear_set= [24, 28, 32, 40, 44, 48, 56, 64, 72, 86]
r= get_gear_set_ratio(56, 57)
```
Run the program. The program will output the following:
```
Spindle 40 -- Worm 56
```

Note: Make necessary interpretation regarding the sign of (A-N) and whether an idle gear should be used or not. Use simple Indexing program to find crank movement.

## GUI program:
I had a plan to make GUI for this program but due to time constraint I couldn't finish. Although I had somewhat drafted the design. In future, I might complete this unfinished project.

![image](https://user-images.githubusercontent.com/47505877/180083056-72a5b872-9f87-40ac-a79a-1545aef7ad77.png)
