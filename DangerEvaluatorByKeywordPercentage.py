# Initialize an empty List ready to be filled with user input
Posts = []
# Inform the user how to exit the upcoming loop
print("To Complete Input, type quit")

message = ""
# Start a loop which will collect Tweets from the user - loop will end when user inputs quit.
while message != "quit":
    message = input("Please enter your tweet. ").lower()
    if message != "quit":
        Posts.append(message)

# List of Words to Count
Safe_Words = ["sunshine"]                             # Safe Words we want to keep track of
Dangerous_Words = ["explosives", "chaos", "bomb"]     # Dangerous Words we want to keep track of

# Create a dictionary to store the count of each hashtag, starting at 0
Safe_Counts = {"sunshine": 0}
Dangerous_Counts = {"explosives": 0, "chaos": 0, "bomb": 0}

# Loop through each post in the list of posts
for Post in Posts:
    # Loop through each Safe Hashtag we are tracking
    for Safe_Hashtag in Safe_Words:
        # Check if the current Hashtag is in the current post
        if Safe_Hashtag in Post:
            Safe_Counts[Safe_Hashtag] += 1  # Increment the Safe Count by 1 for this Hashtag
    # Loop through each Dangerous Hashtag we are tracking
    for Dangerous_Hashtag in Dangerous_Words:
        # Check if the current Hashtag is in the current post
        if Dangerous_Hashtag in Post:
            Dangerous_Counts[Dangerous_Hashtag] += 1  # Increment the Dangerous Count by 1 for this Hashtag

# Calculate total counts by adding up the counts from the Safe and the Dangerous Words
Total_Count = sum(Safe_Counts.values()) + sum(Dangerous_Counts.values())

SafeKeywordPercentage = round((sum(Safe_Counts.values()) / Total_Count) * 100, 2)
DangerousKeywordPercentage = round((sum(Dangerous_Counts.values()) / Total_Count) * 100, 2)

# Print the Final counts for each Hashtag and the Percentage from the total count of Words
print("Safe Hashtag counts:", Safe_Counts, "Safe percentage of Words used:", SafeKeywordPercentage, "%")
print("Dangerous Hashtag counts:", Dangerous_Counts, "Dangerous percentage of Words used:", DangerousKeywordPercentage, "%")

if(DangerousKeywordPercentage > 33.3):
    print("This suspect is classified as potentially dangerous.")
