"""
Estimate: 60 min
Actual:
"""
import datetime
from project import Project

display_list = []

in_file = open("projects.txt", "r")
print("- (L)oad projects  \n- (S)ave projects  \n- "
      "(D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit")
user_choice = input(">>> ").upper()
while user_choice != "Q":
    if user_choice == "L":
        user_file = input("File name: ")
        in_file = open(user_file, "r")
    if user_choice == "S":
        pass
    if user_choice == "D":
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            projects = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            display_list.append(projects)
        display_list.sort()
        for i in display_list:
            print(i)
    if user_choice == "F":
        filter_data = input("")
    if user_choice == "A":
        pass
    if user_choice == "U":
        pass
    print("- (L)oad projects  \n- (S)ave projects  \n- "
          "(D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit")
    user_choice = input(">>> ").upper()

in_file.close()





