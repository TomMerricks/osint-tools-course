import datetime

FirstName = "Tommy Robinson"
DoB = datetime.datetime(1982, 11, 27)
Email = "topbulldog@albionlives.com"
Username = Email.split("@")[0]
Nickname = "Robbo"
Age = 42
Occupation = "Scum"
Followers = 1500
Following = 2345
Recent_Tweet = "England for English"

Followers += 500
Difference = Following-Followers

print(Followers)
print(Difference)
print(Username) #Expected Output: topbulldog



