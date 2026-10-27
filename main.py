"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
from email.mime import base


SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
HOURS_OF_SLEEP_NEEDED_PER_DAY = 8
DAYS_PER_WEEK = 7
HOURS_OF_CLASS_PER_CREDIT = 1
TOTAL_HOURS_PER_WEEK = 168
TOTAL_HOURS_OF_STUDYING_AND_HOMEWORK_PER_CREDIT = 2
LUNCH_DINNER_AND_PERSONAL_CARE_HOURS_PER_DAY = 3



# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / CLASS_DAYS_PER_SEMESTER / SEMESTERS_PER_YEAR


def cost_per_credit(annual_cost, credits_this_semester):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost / credits_this_semester / SEMESTERS_PER_YEAR


def cost_per_class(annual_cost, credits_this_semester):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits_this_semester) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER

def free_time_per_week(credits_this_semester):
    """Give back how many hours of free time you have per week."""
    # Each credit is 1 hour of class per week, and each credit is 2 hours of homework per week.
    # There are 168 hours in a week.
    # Average time to sleep is 8 hours per day, and there are 7 days in a week.
    # Average time for lunch, dinner, and other personal care is 3 hours per day, and there are 7 days in a week.
    return TOTAL_HOURS_PER_WEEK - (HOURS_OF_SLEEP_NEEDED_PER_DAY * DAYS_PER_WEEK + credits_this_semester * HOURS_OF_CLASS_PER_CREDIT + credits_this_semester * TOTAL_HOURS_OF_STUDYING_AND_HOMEWORK_PER_CREDIT + LUNCH_DINNER_AND_PERSONAL_CARE_HOURS_PER_DAY * DAYS_PER_WEEK)


def menu():
    """Display the menu of options."""
    print("\nYour options are:\n 1. Cost per semester\n 2. Cost per month\n 3. Cost per class day\n 4. Cost per credit\n 5. Cost per CS 1430 class\n 6. How much free time will you have?\n Q. Quit\n")

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("How much does college cost for one year? "))
    credits_this_semester = int(input("How many credits are you taking this semester? "))

    while True:
    
        menu()

        choice = input("Use the numbers on your keyboard to select the options you would like to see. ")

        if choice == "1":
            # Call the function for option 1 here.
            semester = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${semester:.2f}")
            pass

        elif choice == "2":
            # Call the function for option 2 here.
            month = cost_per_month(annual_cost)
            print(f"Cost per month: ${month:.2f}")
            pass

        elif choice == "3":
            # Call the function for option 3 here.
            day = cost_per_day(annual_cost)
            print(f"Cost per class day: ${day:.2f}")
            pass

        elif choice == "4":
            # Call the function for option 4 here.
            credit = cost_per_credit(annual_cost, credits_this_semester)
            print(f"Cost per credit: ${credit:.2f}")
        
            pass

        elif choice == "5":
            # Call the function for option 5 here.
            class_cost = cost_per_class(annual_cost, credits_this_semester)
            print(f"Cost per CS 1430 class: ${class_cost:.2f}")

            pass

        elif choice == "6":
            free_time = free_time_per_week(credits_this_semester)
            print(f"Free time per week: {free_time_per_week(credits_this_semester):.2f} hours")

            pass

        

        elif choice == "Q":
            print("Thanks for running the numbers!")
            break

        # Add a branch for each menu option here.
        else:
            print("Invalid choice. Please try again.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()