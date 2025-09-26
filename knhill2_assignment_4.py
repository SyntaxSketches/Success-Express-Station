student_name = "Kabijah"
current_gpa = 3.2
study_hours = 23
social_points = 15
stress_level = 20

print("Welcome to the Success Express Station!")
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

study_options = ["Calculus I", "Python Programming", "English 101", "Art Appreciation"]
print("\nChoose a subject to focus your study on:")
print(", ".join(study_options))
subject = input("Your choice: ")

if subject in study_options:
    if subject == "Python Programming" and current_gpa < 3.0:
        current_gpa += 0.5
        study_hours += 10
        print("Your GPA jumped thanks to coding practice.")
    elif subject == "English 101":
        social_points += 10
        stress_level -= 5
        print("You connected with classmates in this course!")
    elif subject == "Art Appreciation":
        study_hours -= 5
        stress_level += 10
        current_gpa -= 0.1
        print("What a useless class. Extra projects drained your time and GPA slipped.")
    elif subject == "Calculus I" and (stress_level < 40 and current_gpa >= 3.0):
        stress_level += 15
        current_gpa += 0.3
        print("It was tough but rewarding, you’re on track for academic honors.")
    elif subject == "Calculus I" and (stress_level >= 40 or current_gpa < 3.0):
        stress_level += 25
        current_gpa -= 0.2
        print("Calculus I piled on the stress, and it didn’t quite click. Rough semester!")
    else:
        print("That subject isn’t on the train schedule. ")

if type(stress_level) is int:
    print("Stress level tracked correctly")

# Endings
if current_gpa >= 3.8 and study_hours > 40 and social_points >= 30 and stress_level <= 50:
    print("You have arrived at Valedictorian Vista: From the balcony of success, your future streches beyond the horizon. Congrats on highest honors.")

elif 3.5 <= current_gpa <= 3.75:
    print("Welcome to Prestige Point: Where excellence is eanred, despite all the stress, you did it. Congrats")

elif current_gpa >= 3.2 and stress_level <= 25 and social_points < 20:
    print("Welcome to Easy Street: Where the sun always shining, not a cloud in the sky, like you.  You layed lowed, but made it. Congrats on Dean's List")

elif social_points >= 40 and current_gpa < 3.2:
    print("You've arrived at Social SkyWalk: You built an amazing social network, but academics crumbled. You still have a chance ")

elif current_gpa < 2.0:
    print("Welcome to Rebel Rock: The parties never stopped, but you did. You’ve hit academic probation. /You now may sit and think about your actions.")










