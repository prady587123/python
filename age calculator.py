from datetime import date

def calculateAge(birthdate):
    days_in_year = 365.2425
    age = int((date.today()-birthdate).days/days_in_year)
    return age
print(calculateAge(date(1997,2,3)),"years")