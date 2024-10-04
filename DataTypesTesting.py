Bank_Balance = 4.89
New_Motorbike_Cost = 8956.78
Difference = New_Motorbike_Cost - Bank_Balance
print(Difference)

Transaction1 = "5000"
Transaction2 = "12000.50"
Total = int(Transaction1) + float(Transaction2)
print(Total) #Expected Outcome

Name = "Alice"
Age = 30
print(f"Name: {Name}, Age: {Age}")

Keywords_Found = 3
Near_Sensitive_Location = True
print(int(Keywords_Found)," keywords have been found. The suspect has been found in a sensitive location =", bool(Near_Sensitive_Location))

Suspicious_Usernames = ["User123", "Anonymous_456", "StrangeUser789"]
print("Initial List:", Suspicious_Usernames)
Suspicious_Usernames.append("NewSuspiciousUser")
print("After appending:", Suspicious_Usernames)
Count = Suspicious_Usernames.count("Anonymous_456")
print("Occurences of 'Anonymous_456':", Count)
Suspicious_Usernames.insert(0, "HighPriorityUser")
print("After inserting high priority username:", Suspicious_Usernames)
Suspicious_Usernames.remove("Anonymous_456")
print("After removing 'Anonymous_456':", Suspicious_Usernames)
