# Problem Solving Organizer

Technical interviews for data science or software engineer positions often involve problem solving / coding questions.
One might also want to solve such problems for fun! This repo aims at organizing and keeping track of
the different problems solved / to solve.

# Structure

./
    db.json
    generate.py
    check_solved.py
    unsolved_problems.py
    clear_db.py
    problem_generator.py
    
    misc/
        my_problem_name_1/
            readme.md
            solution.py
    my_problem_type/
        my_problem_name_2/
            readme.md
            solution.py
        
Every problem has a:

* type
* name
* description

and is stored in /problem_type/problem_name/ where live at least two files:

* readme.md, where the description is written
* solution.py, ideally executable to give the solution, or at least have a solve() function somewhere

db.json is a "database", storing the problem's type, name, description, as well as a binary value indicating whether
a solution has been found or not yet.