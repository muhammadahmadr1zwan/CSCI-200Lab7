# Function to calculate letter grade based on the input score
def calculate_letter_grade(score):
    if score >= 90: # if score is greater than or equal to 90
        return 'A'; # return A
    elif score >= 80: # if score is greater than or equal to 80
        return 'B'; # return B
    elif score >= 70: # if score is greater than or equal to 70
        return 'C'; # return C
    elif score >= 60: # if score is greater than or equal to 60
        return 'D'; # return D
    else: # otherwise
        return 'F'; # return f

# Function to get the number of students from user input
def get_num_students(): # define get number of students function
    while True: # while this is true
        try: # try 
            num_students = int(input("Enter the number of students (more than 5 only): ")); # number of students is equal to giving an integer input prompt of entering the number of students
            if num_students > 5: # if the inputted value is less than 5
                return num_students; # return the number of students
            else: # otherwise
                print('Invalid input, please enter more than 5 students.'); # print 'Invalid input, please enter more than 5 students.'
        except ValueError: # if there is an error in the value inputted
            print('Invalid input, please enter a valid number.'); # print 'Invalid input, please enter a valid number.'

# Function to input student names and scores and return a dictionary with student names as keys and scores as values
def studentinput_values(num_students): # define student input values function with number of students as a parameter
    student_grades = {};  # Dictionary to store student grades
    for i in range(num_students): # for i in the range of number of students
        name = input(f"Enter full name of student {i + 1}: "); # name is equal to input 'Enter full name of the student'
        score = int(input(f"Enter score for student {name}: ")); # score is equal to the integer input 'Enter score for student'
        student_grades[name] = score; # student_grades function with name as a parameter
    return student_grades; # return student grades

# Function to search students by name and return results with letter grades
def search_student_by_name(student_grades, search_name): # define search student by name function with student grades and search name as parameters
    search_results = {}; # Dictionary to store search results for name
    if search_name in student_grades: # if search in student grades
        search_results[search_name] = calculate_letter_grade(student_grades[search_name]); # student_results function with search name as a parameter is equal to calculate_letter_grade function with student grades and search name as parameters
    return search_results; # return search results

# Function to search students by score and return results with letter grades
def search_student_by_score(student_grades, search_score): # define search student by score function with student grades and search score as parameters
    search_results = {}; # Dictionary to store search results for score
    for student, score in student_grades.items(): # for student, score in student grades.items (function is called)
        if score == search_score: # if score is equal to search score 
            search_results[student] = calculate_letter_grade(score); # search results with the student parameter is equal to calculate letter grade with score as a parameter
    return search_results; # return search results 
