# Data Type - LIST

states_of_america = ["Hawaii", "Alaska", "Washington", "Orego", "California", "Nevada","Idaho", "Arizona", "Utah", "Montana", "Wyoming", "Colorado", "New Mexico", 
                     "North Dakota", "South Dakota", "Nebraska", "Kansas", "Oklahoma", "Texas", "Minnesota", "Iowa", "Missouri", "Arkansas",
                     "Wisconsin", "Illinois", "Michigan", "Indiana", "Ohio", "Kentucky", "Tennessee", "Mississippi", "Alabama", "Louisiana", "Georgia", "Florida", "South Carolina", "North Carolina",
                     "West Virginia", "Virginia", "Delaware", "Maryland", "New York", "Pennsylvania", "New Jersey", "Connecticut", "Rhode Island", "Massachusetts", "Vermont", "New Hampshire", "Maine"
]

print(len(states_of_america))

# Breakdown by general region

pacific = ["Hawaii", "Alaska", "Washington", "Orego", "California", "Nevada", "Arizona", "Idaho", "Utah", "Montana", "Wyoming", "Colorado", "New Mexico"]
mountains_plains_middle = ["North Dakota", "South Dakota", "Nebraska", "Kansas", "Oklahoma", "Texas", "Minnesota", "Iowa", "Missouri", "Arkansas"]
south_east = ["Wisconsin", "Illinois", "Michigan", "Indiana", "Ohio", "Kentucky", "Tennessee", "Mississippi", "Alabama", "Louisiana", "Georgia", "Florida", "South Carolina", "North Carolina"]
north_east = ["West Virginia", "Virginia", "Delaware", "Maryland", "New York", "Pennsylvania", "New Jersey", "Connecticut", "Rhode Island", "Massachusetts", "Vermont", "New Hampshire", "Mainey"]


north_east[-1] = "Maine"
print(north_east[-1])

# List methods - .append(x) , .extend([x,y])

north_east.append("new_state1")
mountains_plains_middle.extend(["new_state2","new_state3"])

print(north_east[-1])
print(north_east)
print(mountains_plains_middle)