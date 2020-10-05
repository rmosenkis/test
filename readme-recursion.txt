Ryan Mosenkis

In this program, I used recursion to find all possible paths to get from one point to another in a maze. I did this by checking the spaces to the north, south, east, and west of the current space to see if that space was empty. If it was, then move to that space and repeat the process until you get to the exit space.

Outputs for the three test cases:
1. 
maze = maze1.dat, start = (2,3), exit = (11,1)
output:
Enter the name of the maze file ("none" if  using random file): maze1.dat
maze1.dat
-------- The Original Maze --------
 012345678901
0*** ********
1***    *****
2*** **  ****
3***   *  ***
4***** ** ***
5***** ** ***
6***** ******
7*****   ****
8***   * ****
9*   **  ****
0* *    *****
1* **********

Please enter the starting row : 2
2

Please enter the starting column : 3
3

Please enter the exiting row : 11
11

Please enter the exiting column : 1
1
It's a path!
 012345678901
0*** ********
1***    *****
2***!**  ****
3***!!!*  ***
4*****!** ***
5*****!** ***
6*****!******
7*****!  ****
8***!!!* ****
9*!!!**  ****
0*!*    *****
1*!**********
It's a path!
 012345678901
0*** ********
1***    *****
2***!**  ****
3***!!!*  ***
4*****!** ***
5*****!** ***
6*****!******
7*****!!!****
8***   *!****
9*!!!**!!****
0*!*!!!!*****
1*!**********

2. 
maze = maze2.dat, start = (4,8), exit = (9,1)
output:
Enter the name of the maze file ("none" if  using random file): maze2.dat
maze2.dat
-------- The Original Maze --------
 012345678901
0************
1***    *****
2*** **  ****
3***   *  ***
4***** ** ***
5***** ** ***
6***** ******
7*****   ****
8****  * ****
9*   **  ****
0* *    *****
1************

Please enter the starting row : 4
4

Please enter the starting column : 8
8

Please enter the exiting row : 9
9

Please enter the exiting column : 1
1
It's a path!
 012345678901
0************
1***!!!!*****
2***!**!!****
3***!!!*!!***
4*****!**!***
5*****!** ***
6*****!******
7*****!!!****
8****  *!****
9*!!!**!!****
0* *!!!!*****
1************

3. 
maze = maze3.dat, start = (0,4), exit = (1,2)
output:
Enter the name of the maze file ("none" if  using random file): maze3.dat
maze3.dat
-------- The Original Maze --------
 012345678901
0* *  * **** 
1**  **  ** *
2 ********   
3**   * *   *
4*  **     **
5****  ****  
6 *  * * *  *
7 *    ****  
8 *   ** * **
9  ** ***  * 
0 * * * *    
1 ***  ***   

Please enter the starting row : 0
0

Please enter the starting column : 4
4

Please enter the exiting row : 1
1

Please enter the exiting column : 2
2
It's a path!
 012345678901
0* *!!* **** 
1**!!**  ** *
2 ********   
3**   * *   *
4*  **     **
5****  ****  
6 *  * * *  *
7 *    ****  
8 *   ** * **
9  ** ***  * 
0 * * * *    
1 ***  ***   

4. 
maze = maze4.dat, start = (10,2), exit = (3,5)
output:
Enter the name of the maze file ("none" if  using random file): maze4.dat
maze4.dat
-------- The Original Maze --------
 012345678901
0************
1************
2************
3************
4************
5************
6************
7************
8************
9************
0** *********
1************

Please enter the starting row : 10
10

Please enter the starting column : 2
2

Please enter the exiting row : 3
3

Please enter the exiting column : 5
5
There are no paths

This is an interesting case test because there will never be a path from (10,2) unless the exit is also at (10,2). Since every space is blocked off besides (10,2), there is no where for the mouse to travel within the maze.