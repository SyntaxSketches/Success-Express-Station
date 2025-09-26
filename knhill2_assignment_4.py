student_name = "YourName"
current_gpa = 3.2
study_hours = 23
social_points = 15
stress_level = 20

print("🚂 Welcome to the Success Express Station!")
print(f"Student: {student_name}")
print(f"Starting GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress: {stress_level}")
#blah blah blah step 2
print("\nChoose your course load:")
print("A) Light Load (12 credits)")
print("B) Standard Load (15 credits)")
print("C) Heavy Load (18 credits)")

choice = input("Your choice: ")
if choice == "A":
    stress_level -= 5
    social_points += 10
    print("Hooray for no stress, success!")
elif choice == "B":
    study_hours += 10
    stress_level += 5
    print("Good choice! Balance goes a long way.")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 20
        stress_level += 15
        print("This is more than the average, but nothing's impossible. You got this!  ")
else:
    print("Invalid choice!")









