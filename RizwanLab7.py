#This program is for Muhammad Rizwan's Lab 8 Assignment for Computing I
#This program will be a Student Information Management System (SIMS) where a user can input a list of students and their scores and the program will output the letter grade
#from the listed scores using a dictionary key and value method.

# Import all functions from the utility file
from Lab7UtilityFile import *;

# Function to display original student grades
def display_student_grades(student_grades): # define display student grades function with student grades as a parameter
    print("Original Student Grades:"); # print 'Original Student Grades: '
    for student, score in student_grades.items():  # Iterate through the dictionary items (student names and scores)
        print(f"{student}: {score}"); # Print each student's name and score

# Function to search students by score and return results with letter grades
def search_student_by_score(student_grades, search_score): # define search student by score function with student grades and search score as a parameters
    search_results = {};  # Create an empty dictionary to store search results
    for student, score in student_grades.items():  # Iterate through the dictionary items (student names and scores)
        if score == search_score:  # If the score matches the search score
            search_results[student] = calculate_letter_grade(score);  # Add student and corresponding grade to search results dictionary
    return search_results;  # Return the search results dictionary

# Function to search students by name and return results with letter grades
def search_student_by_name(student_grades, search_name): # define search student by name function with student grades and search name as a parameters
    search_results = {};  # Create an empty dictionary to store search results
    if search_name in student_grades:  # If the search name exists in the student grades dictionary
        search_results[search_name] = calculate_letter_grade(student_grades[search_name]);  # Add student and corresponding grade to search results dictionary
    return search_results;  # Return the search results dictionary

# Main function where the program execution starts
def main(): # define main function
    # Print program description
    print('  '); # space
    print('This is a Student Information Management System (SIMS). Input the names of students and their scores in COMPUTING I, and the letter grade will be outputted.');
    print('   '); # space
    # Get the number of students from user input
    num_students = get_num_students();

    # Collect student names and scores using the studentinput_values function
    student_grades = studentinput_values(num_students);

    # Display the original student grades (dictionary structure)
    print("\nOriginal Student Grades:");
    print(student_grades);

    # Ask user for the name to search by
    search_name = input("Enter the full name to search by: ");
    # Search students by name and display results with letter grades
    name_search_results = search_student_by_name(student_grades, search_name);
    print("\nSearch by Name:");
    print(name_search_results);

    # Ask user for the score to search by
    search_score = int(input("Enter the score to search students by: "));
    # Search students by score and display results with letter grades
    score_search_results = search_student_by_score(student_grades, search_score);
    print("\nSearch by Score:");
    print(score_search_results);

# This block ensures that main() is called when the script is run
if __name__ == "__main__":
    main();
