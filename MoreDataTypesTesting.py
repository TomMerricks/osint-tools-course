Hashtags = ["#ConflictZone", "#BreakingNews", "#Alert", "#Crisis"]
for Tag in Hashtags:
    print("Monitoring:", Tag)

Document = "Fraud alert: multiple accounts flagged for suspicious activity."
Keywords = ["Fraud", "suspicious", "alert"]
Count = 0

for Word in Keywords:
    if Word in Document:
        Count += 1
        
print("Keywords found:", Count)

while Count <= 5:
    print("Sus activity count:", Count)
    Count += 1

Transaction_Amount = 1200
Risk_Threshold = 1000
if Transaction_Amount > Risk_Threshold:
    print("High risk transaction detected!")
else:
    print("Transaction is within the safe limit.")

Keyword_Detected = True
Late_Night_Activity = True
if Keyword_Detected and Late_Night_Activity:
    print("Suspicious activity detected!")
else:
    print("No immediate threat.")

Suspicious_Score = 0
Suspicious_Posts = 3
Suspicious_Transactions = 2
Suspicious_Score += Suspicious_Posts * 10
Suspicious_Score += Suspicious_Transactions * 20
print("Suspicious Score:", Suspicious_Score)

Message = "This is a discussion about explosive devices"
Keyword = "explosive"
if Keyword in Message:
    print("Alert: Suspicious activity detected!")
else:
    print("No Suspicious activity.")

Transaction_Amount = 7500

if Transaction_Amount > 10000:
    print("High-risk transaction detected.")
elif Transaction_Amount > 5000:
    print("Medium-risk transaction detected.")
else:
    print("Low-risk transaction.")
    
