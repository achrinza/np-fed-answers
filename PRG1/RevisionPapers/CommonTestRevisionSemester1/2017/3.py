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


def main(student_names: List[str] = None, student_marks: List[float] = None) -> float:
    if student_names is None:
        student_names = [
            "John Tan",
            "Tom Ong",
            "Jane Lim",
            "Jim Ng",
            "Mary Choo",
            "Steve Goh",
            "Anne Lee"
        ]
        
    if student_marks is None:
        student_marks = [
            100,
            75,
            80,
            20,
            50,
            70,
            95
        ]

    def convert_check_length(item) -> int:
        return len(str(item))

    student_names_max_length = len(str(max(student_names, key=convert_check_length)))
    student_marks_max_length = len(str(max(student_marks, key=convert_check_length)))
    student_marks_avg = sum(student_marks) / len(student_marks)

    for student_name, student_mark in zip(student_names, student_marks):
        print("{0:<{1}} {2:<{3}}".format(student_name, student_names_max_length, student_mark, student_marks_max_length))

    print("\nAverage: {:.2f}\n".format(student_marks_avg))

    for student_name, student_mark in zip(student_names, student_marks):
        if student_name.find("Goh") > -1:
            print("{0:<{1}} {2:<{3}}".format(student_name, len(student_name), student_mark, len(str(student_mark))))


# Check if this program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run.
if __name__ == "__main__":
    main()
