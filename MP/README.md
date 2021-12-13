# Comparative Analysis on Solving a Sudoku Puzzle using 3 Different Algorithms

## **How to run demo**

- **NOTE:** This uses python3 and certain libraries need to be installed
- Download `sudokudemo.py` and `demo1.txt`
- Run using

```
python sudokudemo.py demo1.txt
```

## **What is a Sudoku Puzzle?**

A _Sudoku_ is a number puzzle in a 9x9 grid that uses the numbers 1 to 9, with some grid squares already filled in, and the goal is to fill in the remaining blank squares with a number, such that every number is unique in each row, column, and 3x3 subgrid.

<img src="https://www.rd.com/wp-content/uploads/2020/12/Sudoku3.jpg" alt="This is a Sudoku Puzzle" width="200">

## **How can you solve a Sudoku Puzzle?**

### **BACKTRACKING**

_Backtracking_ is a methodical way of trying out various sequences of decisions until one that "works" is found.

#### **_How does this solve a Sudoku puzzle?_**

- Starting from the top-left square of the grid, find an empty square and fill in this square with a number from 1 to 9.
  - If the number adheres to the rules, then move on to the next empty square.
  - If the number has a duplicate in its row, column, or 3x3 grid, then choose the next number from 1 to 9.
  - If all choices from 1 to 9 were checked and contradicted, then go back to the previous square and fill in the next number from 1 to 9.
- Repeat steps until the bottom-right square is reached. (Solution is found)

### **STOCHASTIC SEARCH**

_Stochastic Search_ is an optimization algorithm that incorporates randomness. This is implemented with _Beam Search Algorithm_ that examines a graph by extending the most "promising" node at each level.

#### **_How does this solve a Sudoku puzzle?_**

- Create a series of 10 candidate grids by randomly filling in the empty squares in the puzzle.
- Check how many mistakes each board has.
  - If number is zero, the puzzle is solved
  - If there are mistakes, a set of 4 successors is generated from it by taking two squares in the same row (excluding squares from the original puzzle) and switching their labels
    - Successors are added to the set of candidate grids which is then sorted by the number of mistakes and the 10 grids with the least mistakes are taken
- The process is repeated with the new set of 10 grids until a solution is found.

### **CONSTRAINT PROGRAMMING**

A paradigm that identifies feasible solutions out of a set of candidates where the problem can be modeled in terms of arbitrary constraints.

#### **_How does this solve a Sudoku puzzle?_**

- Create a problem instance
  - Add sudoku input and their indices as variables
  - Add constraints to the problem
    1. No two number in a row should be the same
    2. No two numbers in a column should be the same
    3. No two numbers in a 3x3 grid shold be the same

## **Comparative Analysis**

|                                      | Backtracking                                         | Stochastic Search                            | Constraint Programming                                  |
| ------------------------------------ | ---------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| **Time Complexity**                  | Ο(N<sup>n<sup>2</sup></sup>)                         | O(b\*n<sup>2</sup>)                          | Ο(N<sup>n<sup>2</sup></sup>)                            |
| **Method**                           | Depth-first search                                   | Breadth-first search                         | Depth-first search                                      |
| **No. of Solutions _(if possible)_** | 1                                                    | 1 or none                                    | At least 1                                              |
| **Advantage**                        | Would always find a solution if there is one         | Possibility of finding a solution right away | Finds all possible solutions                            |
| **Disadvantage**                     | May spend a long time assuming a value that is wrong | Unreliable and problematic                   | Higher run time than backtracking if multiple solutions |

## **Conclusion**

The most common algorithm used in solving a Sudoku puzzle is the backtracking algorithm because it is comparatively easier to implement. It is also best used if there is only one solution, because it is the most stable and is faster than constraint programming in this regard. However, it is best to use constraint programming if you are trying to find multiple solutions. It is best to avoid the stochastic search because this is the most unreliable and unstable. Additionally, this has more lines of code than the previous two.

## **References**

- Overall code: https://fse.studenttheses.ub.rug.nl/22745/1/bMATH_2020_HoexumES.pdf.pdf
- Backtracking: https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
- Stochastic Search: https://github.com/ananthamapod/Sudoku
- Constraint Programming: https://gist.github.com/ksurya/3940679
- GeeksForGeeks. (2017, July 16). Sudoku (Explanation) | Backtracking | Set 7 | GeeksforGeeks [Video]. YouTube. https://www.youtube.com/watch?v=l7f9-GNH1j8
- Backtracking algorithm. Programiz. (n.d.). Retrieved from https://www.programiz.com/dsa/backtracking-algorithm.
- Neumann, F., & Witt, C. (2010). Stochastic Search Algorithms. Natural Computing Series, 21–32. doi:10.1007/978-3-642-16544-3_3
- Computerphile. (2020, February 13). Python Sudoku Solver - Computerphile [Video]. YouTube. https://www.youtube.com/watch?v=G_UYXzGuqvM
- What is stochastic search. IGI Global. (n.d.). Retrieved from https://www.igi-global.com/dictionary/stationary-density-stochastic-search-processes/28313.
- Introduction to beam search algorithm. GeeksforGeeks. (2021, July 18). Retrieved from https://www.geeksforgeeks.org/introduction-to-beam-search-algorithm/.
- Google. (n.d.). Constraint optimization. Google. Retrieved from https://developers.google.com/optimization/cp.
- Sudoku puzzles, constraint programming and graph theory. OpenSourc.ES. (n.d.). Retrieved from https://opensourc.es/blog/sudoku/.
- Sudoku: Backtracking-7. GeeksforGeeks. (2021, July 22). Retrieved from https://www.geeksforgeeks.org/sudoku-backtracking-7/.
- Sudoku solver. AfterAcademy. (n.d.). Retrieved from https://afteracademy.com/blog/sudoku-solver.
- Define Beam Search. Javatpoint. (n.d.). Retrieved from https://www.javatpoint.com/define-beam-search.
