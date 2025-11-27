# Dice Roller Simulator

This program will ask you how many times you want to roll a pair of dices and it will show you the aggregated results of each dice and the percentage each number occurs (1 to 6) and also the percentage of the sum of the results for the two dices.

```
=============================================
STATISTICS (Total Rolls: 2)
=============================================
DICE OUTCOMES
Value  | Die 1 #  | Die 1 %  | Die 2 #  | Die 2 % 
----------------------------------------------
1      | 0        | 0.0%     | 0        | 0.0%    
2      | 0        | 0.0%     | 0        | 0.0%    
3      | 0        | 0.0%     | 1        | 50.0%   
4      | 1        | 50.0%    | 0        | 0.0%    
5      | 0        | 0.0%     | 0        | 0.0%    
6      | 1        | 50.0%    | 1        | 50.0%   
SUM OUTCOMES
Value  | Count    | Percentage
------------------------------
2      | 0        | 0.0%     
...
9      | 1        | 50.0%    
10     | 1        | 50.0%    
...
```

Note that the bigger the number of rolls, the closer to the calculated probability it approaches.

This program makes use of multiprocessing and will use all of the CPUs you have in your system.

Run with:

```python3 dice_roller.py```
