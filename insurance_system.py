"""
Program Name: Insurance Quote Generator App
Name: Chris Martinez
File Purpose: Defines the profile object structure and the calculate_quote method
Resources used: Python Crash Course (Chapters 8-11)
Date: July 6, 2026
"""


class Profile:
    """Here is the blueprint or class for my profile object"""
    
    def __init__(self, name, age, car_year, salary, driving_history, accidents):
        """Here we havine the attributes"""
        self.name = name
        self.age = int(age)
        self.car_year = int(car_year)
        self.salary = salary
        self.driving_history = driving_history
        self.accidents = accidents
        self.monthly_rate = 0.0

        