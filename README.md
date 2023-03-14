# nearest_neighbor_algorithm
Cranks the nearest neighbor algorithm to solve the traveling salesman problem.
Run the python file.
Input the number of rows your graph has.
Input the number of columns your graph has.

Input the graph from left to right, hitting [ENTER] after each digit, and replacing each hyphen with a zero.

So if your graph was:
  A B C
A - 1 2
B 1 - 1
C 2 1 -
You would type:
0
1
2
1
0
1
2
1
0

Designate the starting vertex as a character (case insensitive).

If you were to use the graph above and wanted to start from the 'B' vertex:
Please specify the starting vertex: B

The alorithm computes the total cost of the trip and the vertices traversed with the inputted information, then closes.

If you were using all of the above examples:
The vertices traversed are: BACB
The total cost of the trip is: 4
