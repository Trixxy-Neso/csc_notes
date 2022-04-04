# dictionary is mathmatical set w/ no duplicate keys, comes in order

person_1 = {
    "first_name": "Philip",
    "last_name": "Flowers",
    "age": "26",
    "job": "accountant",
    "stats": {
        "vert_jump": "20 feet",
        "max_speed": "3 mph"
    }
}

person_2 = {
    "first_name": "Heath",
    "last_name": "Tims",
    "age": "??",
    "job": "president"

}

print (person_1["first_name"])
print (person_2["last_name"])
people = [person_1, person_2]
for person in people:
    print (person ['first_name'])
    print (person.get ('stats', '??'))


#accessing keys
for key in person_2.keys():
    print (key)

for key, value in person_1.items():
    print (key, value)