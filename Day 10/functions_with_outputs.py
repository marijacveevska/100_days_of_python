def format_name(fname,lname):
    fullname = fname.capitalize() + " " + lname.capitalize()
    return fullname

full_name = input("What is your name? ")
last_name = input("What is your last name? ")

print(format_name(fname=full_name,lname=last_name))