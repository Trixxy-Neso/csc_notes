import re   

# regular expression    -   used to find patterns

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validate (email):
    if re.fullmatch(regex, email):
        print (f"{email} is a valid email.")
    else:
        print (f"{email} is not a valid email.")


validate ("coriell@latech.edu")
validate ("jrs108@latech")