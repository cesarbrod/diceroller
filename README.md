# Dice Roller Simulator

This program will ask you how many times you want to roll a pair of dice and it will show you the aggregated results of each dice and the percentage each number occurs (1 to 6) and also the percentage of the sum of the results for the two dice.

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

```
Simulating 10000000 rolls using 12 CPUs...

=============================================
STATISTICS (Total Rolls: 10000000)
=============================================

DICE OUTCOMES
Value  | Die 1 #  | Die 1 %  | Die 2 #  | Die 2 %
----------------------------------------------
1      | 1666576  | 16.7   % | 1666218  | 16.7   %
2      | 1667450  | 16.7   % | 1667315  | 16.7   %
3      | 1670005  | 16.7   % | 1666749  | 16.7   %
4      | 1664657  | 16.6   % | 1666833  | 16.7   %
5      | 1665387  | 16.7   % | 1667186  | 16.7   %
6      | 1665925  | 16.7   % | 1665699  | 16.7   %

SUM OUTCOMES
Value  | Count    | Percentage
------------------------------
2      | 276905   | 2.8      %
3      | 555102   | 5.6      %
4      | 835153   | 8.4      %
5      | 1112159  | 11.1     %
6      | 1389303  | 13.9     %
7      | 1668116  | 16.7     %
8      | 1389130  | 13.9     %
9      | 1108602  | 11.1     %
10     | 831710   | 8.3      %
11     | 555396   | 5.6      %
12     | 278424   | 2.8      %
```

This program makes use of multiprocessing and will use all of the CPUs you have in your system.

Run with:

```python3 dice_roller.py```
