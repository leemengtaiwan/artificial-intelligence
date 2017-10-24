# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We solve the problem by iterating the following two steps:
- For every unit (row, column, diagonal, square), find naked twins
- Remove peers' digits with those appeared in naked twins

And stop when there is no more change. The reason that why we do it in iterative way is because 
after applying the constraint on twins' peers, the peers may become candidates of 
new naked twins, thus we should **progagate** the constraint further whenever there are new naked
twins appear.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The biggest difference between Diagonal Sudoku and normal Sudoku is that we have to add additional 
constraint (digits in two diagonals should not duplicate neither as other units). After adding the constraint,
the problem solving flow is just like the one solving normal sudoku. 

We will use four techniques to solve the sudoku:
- Single digit elimination
- Naked twins elimaination
- One choice selection
- Search / Simulation


Below is the pesudo code of the program.

```
apply single digit elimination
apply naked twins elimaination
apply one-choice strategy
while there are boxes with multiple digits
    for every digit in the box:
        randomly assign a digit to the box, perform the strategies above as simulation
        if the sudoku is solved
            return answer
        else
            try another digit
```


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - Fill in the required functions in this file to complete the project.
* `test_solution.py` - You can test your solution by running `python -m unittest`.
* `PySudoku.py` - This is code for visualizing your solution.
* `visualize.py` - This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

