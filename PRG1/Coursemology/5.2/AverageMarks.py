#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-Short-Identifier: MIT
# (c) 2019 Rifa I. Achrinza
# This code is licensed under MIT license (See LICENSE.txt for details)

from typing import List

__author__ = "Rifa I. Achrinza"
__copyright__ = "Copyright 2019, Rifa I. Achrinza"
__credits__ = ["Rifa I. Achrinza"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rifa I. Achrinza"
__email__ = "rifa@achrinza.com"
__status__ = "Production"

#Create the lists student_list and mark_list
student_list = ['John', 'Tom', 'Jane', 'Jim', 'Mary', 'Steve', 'Anne']
mark_list = [100, 75, 80, 20, 50, 70, 95]

# Declare function to calculate and return the average mark
def calculate_average(student_list: List[str], mark_list: List[int]) -> float:
    # Loop through each student
    # Generate a loop index using enumerate()
    for i, student in enumerate(student_list):
        # Print each student and their respective marks
        # Pair the students with their marks by using their index
        # ...as the students' index is the same as their mark's index
        print("{}: {}".format(student, mark_list[i]))

    # Calculate the average marks
    # ...by taking the total marks divided by the no. of students
    average = sum(mark_list)/len(mark_list)

    # Return the average marks
    return average

    

# Call the student mark average calculator
# ...and pass the student and mark list
calculate_average(student_list, mark_list)