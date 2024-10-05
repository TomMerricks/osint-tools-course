# List of Posts containing Safe & Dangerous Hashtags
Posts = [
    "Loving the #sunshine and #beach vibes.",               # First Post with two safe hashtags
    "Planning something with #explosives haha #bomb",       # Second Post with two dangerous hashtag
    "Lets create #chaos in the streets! #sunshine"          # Third Post with one dangerous hashtag and one safe hashtag
    "I want to #bomb the Councils office"                   # Fourth Post with one dangerous hashtag
]

# List of Hashtags to Count
Hashtags = ["#sunshine", "#explosives", "#chaos", "#bomb"]
Safe_Hashtags = ["#sunshine"]                               # Safe Hashtags we want to keep track of
Dangerous_Hashtags = ["#explosives", "#chaos", "#bomb"]     # Dangerous Hashtags we want to keep track of

# Create a dictionary to store the count of each hashtag, starting at 0
Safe_Counts = {"#sunshine": 0}
Dangerous_Counts = {"#explosives": 0, "#chaos": 0, "#bomb": 0}

# Loop through each post in the list of posts
for Post in Posts:
    # Loop through each Safe Hashtag we are tracking
    for Safe_Hashtag in Safe_Hashtags:
        # Check if the current Hashtag is in the current post
        if Safe_Hashtag in Post:
            Safe_Counts[Safe_Hashtag] += 1  # Increment the Safe Count by 1 for this Hashtag
    # Loop through each Dangerous Hashtag we are tracking
    for Dangerous_Hashtag in Dangerous_Hashtags:
        # Check if the current Hashtag is in the current post
        if Dangerous_Hashtag in Post:
            Dangerous_Counts[Dangerous_Hashtag] += 1  # Increment the Dangerous Count by 1 for this Hashtag

# Calculate total counts by adding up the counts from the Safe and the Dangerous Hashtags
Total_Count = sum(Safe_Counts.values()) + sum(Dangerous_Counts.values())

# Print the Final counts for each Hashtag and the Percentage from the total count of hashtags
print("Safe Hashtag counts:", Safe_Counts, 
      "Safe percentage of Hashtags used:", round((sum(Safe_Counts.values()) / Total_Count) * 100, 2),"%")
print("Dangerous Hashtag counts:", Dangerous_Counts, 
      "Dangerous percentage of Hashtags used:", round((sum(Dangerous_Counts.values()) / Total_Count) * 100, 2), "%")
