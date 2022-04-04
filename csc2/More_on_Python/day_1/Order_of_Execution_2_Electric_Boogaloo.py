# Another Example of Order of Execution

for a in range (1, 4):                  #1st 10th 19th
    for b in range (1, 5):              #2nd 4th 6th 8th 11th 13th 15th 17th 20th 22nd 24th 26th
        print (f"{a} * {b} = {a*b}")    #3rd 5th 7th 9th 12th 14th 16th 18th 21st 23rd 25th 27th
