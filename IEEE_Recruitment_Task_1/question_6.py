# Marks cutoff list for BITSAT '24
cutoff_list = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Eco", 271),
    ("Pilani", "Msc. Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Eco", 263),
    ("Goa", "Msc. Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Eco", 261),
    ("Hyderabad", "Msc. Bio", 234),
]

 # Initialize an empty dictionary to store cutoff data
cutoff_dict = {}

# Iterate over each tuple in cutoff_list (assumed to be a list of (campus, branch, cutoff) tuples)
for campus, branch, cutoff in cutoff_list:
    # If the campus is not already a key in cutoff_dict, add it with an empty dictionary as its value
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    # Set the cutoff value for the specific branch under the current campus
    cutoff_dict[campus][branch] = cutoff

# Iterate through each campus in the cutoff_dict
for campus in cutoff_dict:
    # Print the campus name and its corresponding branch-cutoff dictionary in a formatted way
    print(f'"{campus}" : {cutoff_dict[campus]},\n')   