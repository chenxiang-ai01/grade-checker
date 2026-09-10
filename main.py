score = int(input("Enter your score: "))

if 85 <= score <= 100:
    print("Excellent")
elif 60 <= score < 85:
    print("Pass")
elif 0 <= score < 60:
    print("Fail")
else:
    print("Invalid score")