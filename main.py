"""
Program Name: Insurance Quote Generator App
Author: Chris Martinez
Program Purpose: A user friendly tool that will ask customers basic questions like their age and driving history,
and then it will calculate their car insurance price depending on their answer, and then it will save that data into a profile.
Resources Used: Python Crash Course (Chapters 1-7)
Date: June 17 2026
"""

from insurance_system import Profile, QuoteCalculator
from data import Data


def show_profiles(all_customers):
   """This function loops through the list of customers and it displays the profiles created"""

   print("---------------- PROFILES CREATED ----------------")

   if not all_customers:
      print("No profiles have been created")
   else:
      for profile in all_customers:

       print("Driver:", profile["Customer Name"], " | Age:", profile["Age"], " | Monthly Rate:", profile["Monthly Rate"])

      print("-------------------------------------------------")


#This replaces my old dictionary list
calculator = QuoteCalculator()
handler = Data()


#Below is my main program loop

running = True
while running == True:

    print("********************************")
    print("   Welcome to MTZ Insurance!   ")
    print("********************************")

    customer_name = input("Please enter your full name, type view to view profiles, or type quit to quit the program: ").strip()

    if customer_name.lower() == 'view':
       all_customers = handler.load_profiles()
       show_profiles(all_customers)
       continue

    if customer_name.lower() == 'quit':
       running = False
       continue


    #User Input Section

    age = int(input("Please enter your age: "))
    car_year = int(input("Please enter the 4 digit year of your car: "))    
    salary = float(input("Please enter your annual salary using only numbers(no commas): "))   
    driving_years = int(input("Please enter the total number of years you have been driving: ")) 
    accidents = int(input("Please enter the total number of car accidents you had: ")) 


    #Updated by building the object and calculate rates using the classes imported

    new_user = Profile(customer_name, age, car_year, salary, driving_years, accidents)
    monthly_payment = calculator.calculate_quote(age, car_year, salary, driving_years, accidents)
    new_user.monthly_rate = monthly_payment

    #Transfer the profile objcet data to a dictionary
    customer_profile = new_user.to_dict()

    #Saves customers profile to JSON file
    handler.save_profiles(customer_profile)


    #Printed out the customers quote result

    print("-----MTZ Insurance Quote-----")
    print("                             ")
    print("Customer Name: " + customer_profile["Customer Name"])
    print("Monthly Rate: $" + str(customer_profile["Monthly Rate"]))
    print("                             ")

#This section is what is displayed when the user exits the loop

print("********************************")
print("Thank you for visiting MTZ Insurance")
print("********************************")






    