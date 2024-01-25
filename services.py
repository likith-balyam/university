"""Services"""

from classes import *
from constants import *

class UniversityServices:
    pass

class StudentServices:
    
    @classmethod
    def get_university(cls, student:Student):
        """Return university."""
        return student.university
        
    @classmethod
    def calculate_no_of_ways_to_attend(cls, student:Student):
        """Student on a day has two choices
           either Attend the class or not attend the class.
        """
        # initialize ways
        ways = ""
        university = cls.get_university(student)
        no_of_classes_cant_miss = university.no_of_classes_cant_miss
        graduation_days = university.graduation_days
        invalid_classes_skip_string = cls.get_skip_classes_identifier(no_of_classes_cant_miss)
        no_of_ways_set=set()
        cls.calculate_ways(graduation_days, ways,graduation_days, no_of_ways_set)
        student.all_ways_to_attend = list(no_of_ways_set)
        student.valid_ways_to_attend = cls.get_ways_without_consecutive_absents(student.all_ways_to_attend, invalid_classes_skip_string)
        student.invalid_ways_to_attend = cls.get_ways_with_consecutive_absents(student.all_ways_to_attend, invalid_classes_skip_string)
        return len(student.valid_ways_to_attend)
    
    @classmethod
    def get_ways_without_consecutive_absents(cls, total_no_of_ways:list, invalid_classes_skip_string:str):
        """Ways without consecutive absents."""
        consecutive_non_absents_list = []
        for way in total_no_of_ways:
            if invalid_classes_skip_string not in way:
                consecutive_non_absents_list.append(way)
        return consecutive_non_absents_list
        
    
    @classmethod
    def get_ways_with_consecutive_absents(cls, total_no_of_ways:list, invalid_classes_skip_string:str):
        """Ways with consecutive absents."""
        consecutive_absents_list = []
        for way in total_no_of_ways:
            if invalid_classes_skip_string in way:
                consecutive_absents_list.append(way)
        return consecutive_absents_list
    
    @classmethod    
    def get_last_day_absents(cls, total_no_of_ways: list):
        """Get last day absenties."""
        last_day_absents = 0
        for way in total_no_of_ways:
            if way and way[-1] == NOT_ATTEND:
                last_day_absents += 1
                
        return last_day_absents
    
    @classmethod
    def get_skip_classes_identifier(cls, no_of_classes_cant_miss:int):
        """Get skip classes identifier."""
        skip_string = ""
        for _ in range(no_of_classes_cant_miss):
            skip_string += NOT_ATTEND
        return skip_string
        
    @classmethod
    def calculate_ways(cls, cur_days:int, ways:str, graduation_days:int, no_of_ways_set:set):
        """Get all possible ways recursively.""" 
        if cur_days == 0 and ways:
            no_of_ways_set.add(ways)
        elif cur_days > 0 and cur_days <= graduation_days:
            cls.calculate_ways(cur_days-1, ways+ATTEND, graduation_days, no_of_ways_set)
            cls.calculate_ways(cur_days-1, ways+NOT_ATTEND, graduation_days, no_of_ways_set)