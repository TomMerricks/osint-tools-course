suspect_1 = {
    "name": "Tommy Robinson",
    "age": "42",
    "address": "123 Red Street",
    "charges": ["Rioting", "Vandalism", "Assault"]
}

suspect_2 = {
    "name": "Ryan Neary",
    "age": "67",
    "address": "456 Right Street",
    "charges": ["Theft", "Vandalism", "DUI"]
}

suspect_3 = {
    "name": "Dave Smith",
    "age": "27",
    "address": "789 Hanger Lane",
    "charges": ["Fraud", "Perjury", "Witness Tampering"]
}

suspect_database = {
    "S1": suspect_1,
    "S2": suspect_2,
    "S3": suspect_3
}

print(suspect_database["S3"]["charges"])

suspect_database["S1"]["charges"].append("Resisting Arrest")

suspect_4 = {
    "name": "Micah Henry",
    "age": "32",
    "address": "67 Straight Road",
    "charges": ["Jaywalking", "Theft"]
}

suspect_database["S4"] = suspect_4

del suspect_database["S1"]

for suspect_id, suspect_info in suspect_database.items():
    print(suspect_info["name"])

# · How would you handle multiple suspects with the same name?
# They have a unique Identifier being S1, S2, S3, etc.

# · What if a suspect has no charges? How would you represent that in the dictionary?
# You could add that as "No Charges" or leave the List Blank/Empty

def find_suspect_by_name(database, name):
    for suspect in database.values():
        if suspect["name"] == name:
            return suspect
        return "Suspect Not found."
    
 # Lets test the function
print(find_suspect_by_name(suspect_database, "Ryan Neary"))             # Expected Outcome: Suspect Information Displayed
print(find_suspect_by_name(suspect_database, "Tom Merricks"))           # Expected Outcome: Suspect Not Found
