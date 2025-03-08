#Act 4 
def assign_grade():
    score = int(input("Enter the student's score: "))

    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
    
    user_input = input("Do you want to check another score? (yes/no): ").lower()
    if user_input == 'yes' or user_input == 'y':
        assign_grade()
    else:
        print("Grade checking skipped.")

assign_grade()
