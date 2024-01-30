import methods

#ask someone what they know (vertical displacement, horizontal displacement, time, initial vertical velocity, final vertical velocity, horizontal velocity)

print("From this list of categories (vertical displacement, horizontal displacement, time, initial vertical velocity, final vertical velocity, horizontal velocity)")

#create empty list of known variables and their corresponding categories
knownDict = {}

#map each case to its corresponding function
functionMapping = {
    ("initial vertical velocity", "time", "vertical displacement"): methods.vertical_Displacement_With_Time,
    ("time", "vertical displacement", "initial vertical velocity"): methods.initial_Vertical_With_Time,
    ("vertical displacement", "initial vertical velocity", "time"): methods.time_With_Vertical_Displacement,
    ("final vertical velocity", "time", "initial vertical velocity"): methods.initial_Velocity_With_Time,
    ("initial vertical velocity", "time", "final vertical velocity"): methods.final_Velocity_With_Time,
    ("final vertical velocity", "initial vertical velocity", "time"): methods.time_With_Final_Velocity,
    ("final vertical velocity", "initial vertical velocity", "vertical displacement"): methods.vertical_Displacement_With_Initial_Velocity,
    ("final vertical velocity", "vertical displacement"): methods.final_Velocity_With_Initial_Velocity,
    ("horizontal velocity", "time"): methods.horizontal_Displacement_With_Time,
    ("time, horizontal displacement"): methods.horizontal_Velocity_With_Time,
    ("horizontal displacement", "horizontal velocity"): methods.time_With_Horizontal_Displacement

}

#take two inputs of category and value from user and store them in a dictionary
for i in range(2):

    key = input("Type in a known category: ")
    value = int(input("Type in the value: "))
    knownDict[key] = value 

    if i !=0:
        key = input("What are you trying to find: ")
        value = "unknown"
        knownDict[key] = value

#get the categories for the if statements
categories = sorted(knownDict.keys())

#if statements to match



print(knownDict)
print(categories)

if tuple(categories) in functionMapping:
    output = functionMapping[tuple(categories)](knownDict[categories[0]], knownDict[categories[1]])
    print(output)
elif tuple(categories) in functionMapping:
    output1 = functionMapping[tuple(categories)](knownDict[categories[1]], knownDict[categories[0]])
    print(output1)
else:
    print("this is not a category combination")






#set up a dictionary 

