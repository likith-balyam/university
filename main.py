"""Main."""

from classes import *
from services import *

if __name__ == "__main__":    
    try:
        print("Enter | seperated values of University: name|graduation_days|no_of_classes_cant_miss")
        university_input = input()
        university_values = university_input.split("|")
        university_name = university_values[0]
        graduation_days = int(university_values[1])
        no_of_classes_cant_miss = int(university_values[2])
        
        if len(university_values) > 3:
            raise Exception("Invalid Input")
        
        print("Enter | seperated values of Student Details: name")
        student_input = input()
        student_values = student_input.split("|")
        if len(student_values) > 1:
            raise Exception("Invalid Input")

        student_name = student_values[0]
        university_obj = University(university_name, graduation_days, no_of_classes_cant_miss)
        student_obj = Student(student_name, university_obj)
        possible_ways = StudentServices.calculate_no_of_ways_to_attend(student_obj)
        missed_graduation = StudentServices.get_last_day_absents(student_obj.valid_ways_to_attend)
        
        # p = no of ways didnt attend the ceremony / total no of valid ways to attend classes (total ways to attend classes)
        print(f"for {graduation_days} days : {missed_graduation}/{possible_ways}")
    except:
        raise Exception("Invalid Input")

            
        
        