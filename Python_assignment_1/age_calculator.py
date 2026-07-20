# ● Read your birth year and calculate your age.
from datetime import date 
def age_cal():
    birth_year=int(input("Enter your birth year : "))
    current_year=date.today().year
    print(f"your age is : {current_year-birth_year}")
age_cal()