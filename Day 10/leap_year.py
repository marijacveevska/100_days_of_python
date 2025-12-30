# Write a program that returns True or False whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# Check the Flow chart jpg

year = int(input("Which year do you want to check if it is Leap or Not Leap? "))

'''Dockstrings are used to add a description 
to a newly created function or some extra info 
about the code so it is visible in the Documentation
'''

def is_leap_year(year):
    
    ''' Checks if a year is 
    leap = True or 
    non leap = False '''

    if year % 4 != 0:
        print(False)
    else:
        if year % 100 != 0:
            print(True)
        else:
            if year % 400 == 0:
                print(True)
            else:
                print(False)

is_leap_year(year)


print(2000%4)
print(2000%100)
print(2000%400)