"""
Program Name: Insurance Quote Generator App
Author: Chris Martinez
Program Purpose: A user friendly tool that will ask customers basic questions like their age and driving history,
and then it will calculate their car insurance price depending on their answer, and then it will save that data into a profile.
Resources Used: Python Crash Course (Chapters 1-7)
Date: June 17 2026
"""

def calculate_quote(age, car_year, salary, driving_years, accidents):
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

def show_profiles(all_customers):
   """This function loops through the list of customers and it displays the profiles created"""

   print("---------------- PROFILES CREATED ----------------")

   if not all_customers:
      print("No profiles have been created")
   else:
      for profile in all_customers:

       print("Driver:", profile["Customer Name"], " | Age:", profile["Age"], " | Monthly Rate:", profile["Monthly Rate"])

      print("-------------------------------------------------")



#Here is my list for all my customers dictionaries stores

all_customers = []


#Below is my main program loop

running = True
while running == True:

    print("********************************")
    print("   Welcome to MTZ Insurance!   ")
    print("********************************")

    customer_name = input("Please enter your full name, type view to view profiles, or type quit to quit the program: ").strip()

    if customer_name.lower() == 'view':
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


    #Here the function is called to find the final insurance price for the customer

    monthly_payment = calculate_quote(age, car_year, salary, driving_years, accidents)

    #Below is a dictionary collection to create a customer profile

    customer_profile = {
       "Customer Name": customer_name,
       "Age": age,
       "Monthly Rate": monthly_payment
    }

    #Here the profile has been appended to the all_customers list

    all_customers.append(customer_profile)

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






    