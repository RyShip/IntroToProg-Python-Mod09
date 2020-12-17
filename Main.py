# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# RShip 12.16.20 used template to complete scrip.
# <Your Name>,<Today's Date>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
from DataClasses import Employee as Emp
from ProcessingClasses import FileProcessor as Fp
from IOClasses import EmployeeIO as Eio


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
lst_data = Fp.read_data_from_file('EmployeeData.txt')
emp_table = []
for row in lst_data:
    emp_table.append(Emp(row[0], row[1], row[2].strip()))
# Show user a menu of options
while True:
    Eio.print_menu_items()
# Get user's menu option choice
    str_choice = Eio.input_menu_options()
    # Show user current data in the list of employee objects
    if str_choice == '1':
        Eio.print_current_list_items(emp_table)

    # Let user add data to the list of employee objects
    elif str_choice == '2':
        emp_table.append(Eio.input_employee_data())

    # let user save current data to file
    elif str_choice == '3':
        Fp.save_data_to_file('EmployeeData.txt', emp_table)

    # Let user exit program
    elif str_choice == '4':
        break

# Main Body of Script  ---------------------------------------------------- #
