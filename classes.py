"""
Classes
"""

class University:
    """University Class."""
    
    def __init__(self, name, days, no_of_classes_cant_miss):
        """University Object Constructor."""
        self.name = name
        self.graduation_days = days
        self.no_of_classes_cant_miss = no_of_classes_cant_miss  # No of class students continuosly cant miss


class Student:
    """Student Class."""
    
    def __init__(self, name, university):
        """Student Object Constructor."""
        self.name = name
        self.all_ways_to_attend = []
        self.valid_ways_to_attend = []
        self.invalid_ways_to_attend = []
        self.university = university
        