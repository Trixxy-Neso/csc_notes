# Sets - unordered grouping without duplicates
a_set = {5, 10, 15, 15, 15, 15, 30, 15, 20}
print (a_set)

a_list = [1, 2, 3, 4, 5, 6, 7, 6, 6, 6, 6, 6, 6, 8]
a_set = set (a_list)
print (a_set)

# union with |, intersection with &, difference with -
print ({1, 2, 3} | {3, 4, 5})
print ({1, 2, 3} & {3, 4, 5})
print ({1, 2, 3} - {2, 3})


# Dictionary - Set of Key:Value Pairs

prof = {
    "first_name":"Josh",
    "last_name":"Coriell", 
    "class":"CompSci"
}
print (prof["first_name"])


# iterate over dictionaries
for key in prof:
    print (key)
for key in prof:
    print(prof[key])
for k,v in prof.items():
    print(k, v)

students = [
    {
        "name":"Jo",
        "age":19,
        "last_name":"Sale",
        "major":"CompSci",
        "hobbies":["patting child", "laying on Tiny Couch"],
        "has_face": False

    },
    {
        "name":"Damien",
        "age":18,
        "last_name":"Sylvester",
        "major":"CompSci",
        "hobbies":["drawing", "enjoing grass"],
        "has_face": True

    },
    {
        "name":"Cristina",
        "age":19,
        "last_name":"Simino",
        "major":"CYEN",
        "hobbies":["piano", "shows"],
        "has_face": True

    },
    {
        "name":"Alex",
        "age":18,
        "last_name":"Jose",
        "major":"CYEN",
        "hobbies":["Blender", "Programming"],
        "has_face": True

    },
    {
        "name":"Josh",
        "age":546789,
        "last_name":"Coriell",
        "major":"NA",
        "hobbies":["Piano", "Games", "Eating"],
        "has_face": True

    }
]

def is_bab (student:dict):
    return student ["age"] < 19

babs = list(filter(is_bab, students))
print (babs)

def letter_writer (student:dict):
    result = f"Hi {student['name']} {student['last_name']},\nI hear you are {student['age']} years old.\nCongrats on majoring in {student['major']}."
    return result

letters = list(map (letter_writer, students))

#for index, letter in enumerate (letters):
#    file = open(f'Letter/{students[index]["last_name"]}.txt', 'w')
#    file.write(letter)
#    file.close()