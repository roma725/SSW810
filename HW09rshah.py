#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roma Shah                        

We will be using 4 data files:
    students.txt:   a tab separated file with 
        CWID   StudentName   Major
        
    instructors.txt:   a tab separated file with 
        CWID   InstructorName   Department
        
    grades.txt: a tab separated file with
        StudentCWID  Course  Grade  InstructorCWID
        
    (FROM HW 10??) majors.txt: a tab separated file with
        Major RequiredCourse
        
In HW09, you will need to read the students, instructors, and grades files
and then use PrettyTable to create summaries of students and instructors:
    
+-------+-------------+-----------------------------------+
|  CWID |     Name    |              Courses              |
+-------+-------------+-----------------------------------+
| 10183 |  Chapman, O |            ['SSW 689']            |
| 11461 |  Wright, U  | ['SYS 611', 'SYS 750', 'SYS 800'] |
| 10172 |  Forbes, I  |       ['SSW 555', 'SSW 567']      |
| 10115 |   Wyatt, X  | ['SSW 564', 'SSW 567', 'SSW 687'] |
| 11658 |   Kelly, P  |            ['SSW 540']            |
| 11788 |  Fuller, E  |            ['SSW 540']            |
| 11714 |  Morton, A  |       ['SYS 611', 'SYS 645']      |
| 11399 |  Cordova, I |            ['SSW 540']            |
| 10175 | Erickson, D | ['SSW 564', 'SSW 567', 'SSW 687'] |
| 10103 |  Baldwin, C | ['SSW 564', 'SSW 567', 'SSW 687'] |
+-------+-------------+-----------------------------------+

+-------+-------------+------+---------+----------+
|  CWID |     Name    | Dept |  Course | Students |
+-------+-------------+------+---------+----------+
| 98764 |  Feynman, R | SFEN | SSW 687 |    3     |
| 98764 |  Feynman, R | SFEN | SSW 564 |    3     |
| 98760 |  Darwin, C  | SYEN | SYS 750 |    1     |
| 98760 |  Darwin, C  | SYEN | SYS 800 |    1     |
| 98760 |  Darwin, C  | SYEN | SYS 611 |    2     |
| 98760 |  Darwin, C  | SYEN | SYS 645 |    1     |
| 98765 | Einstein, A | SFEN | SSW 567 |    4     |
| 98765 | Einstein, A | SFEN | SSW 540 |    3     |
| 98763 |  Newton, I  | SFEN | SSW 555 |    1     |
| 98763 |  Newton, I  | SFEN | SSW 689 |    1     |
+-------+-------------+------+---------+----------+
"""

import os
from collections import defaultdict
from prettytable import PrettyTable
from HW08FRrshah import file_reader
import unittest

class University:
    """ Store all information about students and instructors """ 
    def __init__(self, wdir, ptables=True):
        self._wdir = wdir  # directory with the students, instructors, and grades files
        self._students = dict()  # key: cwid value: instance of class Student
        self._instructors = dict()  # key: cwid value: instance of class Instructor

        self._get_students(os.path.join(wdir, 'students.txt'))
        self._get_instructors(os.path.join(wdir, 'instructors.txt'))
        self._get_grades(os.path.join(wdir, 'grades.txt'))

        if ptables:
            print("\nStudent Summary")
            self.student_table()
    
            print("\nInstructor Summary")
            self.instructor_table()  

    def _get_students(self, path):
        """ read students from path and add the to self.students """
        try:
            for cwid, name, major in file_reader(path, 3, sep='\t', header=False) :
                self._students[cwid] = Student(cwid, name, major)
        except ValueError as e:
            print(e)

    def _get_instructors(self, path):
        """ read instructors from path and add the to self.instructors """
        try:
            for cwid, name, dept in file_reader(path, 3, sep='\t', header=False):
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except ValueError as e:
            print(e)
                
    def _get_grades(self, path):
        """ read grades files and attribute the grade to the appropriate student and instructor """
        try:
            for student_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='\t', header=False):                
                if student_cwid in self._students:
                    self._students[student_cwid].add_course(course, grade)
                else:
                    print(f"Found grade for unknown student '{student_cwid}'")
                
                if instructor_cwid in self._instructors:
                    self._instructors[instructor_cwid].add_student(course)
                else:
                    print(f"Found grade for unknown instructor '{instructor_cwid}'")
        except ValueError as e:
            print(e)
                
    def student_table(self):
        """ print a PrettyTable with a summary of all students """
        pt = PrettyTable(field_names=Student.pt_hdr)
        for student in self._students.values():
            pt.add_row(student.pt_row())
        
        print(pt)
        
    def instructor_table(self):
        """ print a PrettyTable with a summary of all instructors. """
        pt = PrettyTable(field_names=Instructor.pt_hdr)
        for instructor in self._instructors.values():
            # each instructor may teach many classes
            for row in instructor.pt_rows():
                pt.add_row(row)
        
        print(pt)

        
class Student:
    """ Represent a single student"""
    pt_hdr = ["CWID", "Name", "Completed Courses"]

    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()  # key: courses value: str with grade
        
    def add_course(self, course, grade):
        """ Note that the student took a course """
        self._courses[course] = grade

    def pt_row(self):
        """ return a list of values to populate the prettytable for this student """
        return [self._cwid, self._name, sorted(self._courses.keys())]
        
        
class Instructor:
    """ represent an instructor """
    pt_hdr = ["CWID", "Name", "Dept", "Course", "Students"]

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)  # key: course value: number of students
        
    def add_student(self, course):
        """ Note that another student took a course with this instructor """
        self._courses[course] += 1

    def pt_rows(self):
        """ A generator returning rows to be added to the Instructor prettytable """
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]

        
def main():
    wdir = '/Users/jrr/Documents/Stevens/810/Assignments/Repository'
    stevens = University(wdir)
    #nyu = University('/Users/Class2018/Documents/Visual Studio 2012/SSW 810/Repository')


class UniversityTest(unittest.TestCase):
    def stevens(self):
        wdir = '/Users/Class2018/Documents/Visual Studio 2012/SSW 810/Repository'
        stevens = University(wdir)
        expect_students = None
        expect_instructors = None

        students = [s.pt_row() for s in stevens._students]
        instructors = [row for instructor in stevens._instructors.values() for row in instructor.pt_rows()]
    
        self.assertEqual(students, expect_students)
        self.assertEqual(instructors, expect_instructors)

if __name__ == '__main__':
    main()