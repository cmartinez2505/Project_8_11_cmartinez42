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

    def to_dict(self):
        """This stores the object data into a dictionary for JSON"""
        return {
            "Customer Name": self.name,
            "Age": self.age,
            "Monthly Rate": round(self.monthly_rate, 2)
        }    

class QuoteCalculator:
    """Checks parameters to make the monthly quote"""

    def calculate_quote(self, age, car_year, salary, driving_years, accidents):
        """This function calculates the final monthly insurance cost based on customer information and driving history"""
        base_insurance = 100.00
        in_progress = base_insurance

        #If Statement #1 (A surcharge of $25 for young drivers that are 25 and under.)
        if age <= 25:
               in_progress += 25.00
        else:
            pass;   

        #If Statement #2 (A discount of $15 for cars older then 15 years old and a $15 addition for cars newer 2023.)
        if car_year <= 2011:
         in_progress -= 15.00
        elif car_year >= 2024:
         in_progress += 15.00
        else:
         pass

        #If Statement #3 (A 10 percent surcharge is given for those who make over $200,000 annualy and a 10 discount for those who make $40,000 or less a year.)
        if salary >= 200000:
         in_progress += in_progress * 0.10
        elif salary <= 40000:
         in_progress -= in_progress * 0.10    
        else:
         pass

        #If Statement #4 (A extra 10 percent discount is given to drivers who drove a car for atleast 5 years or more.)
        if driving_years >= 5:
         in_progress -= in_progress * 0.10
        else:
         pass

        #If Statement #5 (A extra 5 percent surcharge is given for those who had gotten into 2 or more car accidents.)
        if accidents >= 2:
         in_progress += in_progress * 0.05
        else:
         pass

        return in_progress

