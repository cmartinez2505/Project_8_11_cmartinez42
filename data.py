"""
Program Name: Insurance Quote Generator App
Name: Chris Martinez
File Purpose: Being able to read and save data into a JSON file
Resources used: Python Crash Course (Chapters 8-11)
Date: July 7, 2026
"""

import json

FILENAME = "profiles.json"

class Data:
    """This class is used to read and write customer data files"""

    def load_profiles(self):
        """This function will try to open the JSON file and return the lists"""
        try:
            with open(FILENAME, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_profiles(self, new_profile):
        """This fuction will load already made profiles, append the new profile, then save it all""" 

        profiles = self.load_profiles()
        profiles.append(new_profile)

        with open(FILENAME, 'w') as f:
            json.dump(profiles, f)