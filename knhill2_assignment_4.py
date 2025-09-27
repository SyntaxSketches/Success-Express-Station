
# Help/Guidance: Used ChatGPT (GPT-5-mini) for debugging syntax issues, 
#                grade calculation logic, and suggestions for branching and endings.

git add knhill2_assignment_4.py README.md
git commit -m "Initial commit: foundation code and variables"

student_name = "Kabijah"
# Starting values (can be changed for testing different outcomes)
current_gpa = 2.9
study_hours = 10
social_points = 10
stress_level = 5

# Hidden course grades (float GPA values per course)
course_grades = []

# Function: assign_grade
# Converts performance (study, stress, gpa_boost) into a course GPA value.
def assign_grade(study, stress, gpa_boost):
    """
    Assigns a grade based on study hours, stress, and a small gpa boost.
    Returns a numeric GPA value between 1.0 and 4.0.
    """
    # performance formula — tuned so choices matter and GPA can swing
    score = study - (stress // 2) + gpa_boost
    if score >= 30:
        return 4.0  # A
    elif score >= 25:
        return 3.5  # B+
    elif score >= 20:
        return 3.0  # B
    elif score >= 15:
        return 2.0  # C
    else:
        return 1.0  # D/F

# Intro (original wording kept)
print(f"Welcome to Success Express Station!")
print(f"Student: {student_name}")
print(f"Starting GPA:{current_gpa} \nStudy Hours:{study_hours} \nSocial Points: {social_points} \nStress: {stress_level} ")

# ================== Stop 1: Course Load (original text) ==================
print("\n Stop 1: Choose your course load!:" )
print("Light Load (12 credits)")
print("Standard Load (15 credits)")
print("Heavy Load (18 credits):")

# For testing / zyBooks, we use an automatic choice variable.
# Replace these strings with input() when you want interactive play.
choice = "Light Load"  # testing default

if choice == "Light Load":
    study_hours += 5
    stress_level -= 5
    social_points += 5
    print("Hooray for no stress, success!")
elif choice == "Standard Load":
    study_hours += 20
    stress_level += 5
    social_points += 5
    print("Good choice! Balance goes a long way.")
elif choice == "Heavy Load":
    study_hours += 35
    stress_level += 15
    social_points += 5
    print("This is more than the average, but nothing's impossible. You got this!  ")
# Use 'not in' membership operator to catch invalid choice input — natural spot.
if choice not in ["Light Load", "Standard Load", "Heavy Load"]:
    print("Invalid Choice!")

# ================== Multi-course flow (keeps original flavor) ==================
# We'll run all four courses in order (Python, English 101, Calculus I, Art Appreciation).
# Each course uses your original text and effects, but also appends a numeric grade.

git add knhill2_assignment_4.py
git commit -m "Course planning: course load and subject flows"


# --- Course 1: Python ---
print("\nFirst course: Python Programming")
# Keep your original logic but applied in multi-course flow:
if current_gpa < 3.3:
    current_gpa += 0.6
    study_hours += 15
    stress_level += 10
    social_points += 2
    print("Your GPA jumped thanks to coding practice.")
else:
    study_hours += 5
    stress_level += 3
    current_gpa += 0.2
    print("You practiced coding and solidified your skills.")
# Hidden grade calculation for Python (gpa_boost = 2)
course_grades.append(assign_grade(study_hours, stress_level, 2))

# --- Course 2: English 101 ---
print("\nSecond course: English 101")
social_points += 15
stress_level -= 5
study_hours += 5
current_gpa += 0.1
print("You connected with classmates in this course!")
# Hidden grade calculation for English (gpa_boost = 1)
course_grades.append(assign_grade(study_hours, stress_level, 1))

# --- Course 3: Calculus I ---
print("\nThird course: Calculus I")
if stress_level < 40 and current_gpa >= 3.0:
    study_hours += 20
    stress_level += 20
    current_gpa += 0.4
    print("It was tough but rewarding, you’re on track for academic honors.")
else:
    study_hours += 10
    stress_level += 25
    current_gpa -= 0.2
    print("Calculus I piled on the stress, and it didn’t quite click.")
# Hidden grade calculation for Calculus (gpa_boost = 0)
course_grades.append(assign_grade(study_hours, stress_level, 0))

# --- Course 4: Art Appreciation ---
print("\nFourth course: Art Appreciation")
study_hours -= 5
stress_level += 15
current_gpa -= 0.3
social_points += 8
print("Extra projects drained your time and GPA slipped.")
# Hidden grade calculation for Art (gpa_boost = -1)
course_grades.append(assign_grade(study_hours, stress_level, -1))

git add knhill2_assignment_4.py
git commit -m "Study strategy: mid-semester choices & grade calc"

# ================== Mid-semester choices (kept original) ==================
print("\nDo you want to go on a Coffee Run?")
# For automated runs, default to "Yes" or "No" — here we use a testing default
coffee_choice = "Yes"  # change to input() for real play
if coffee_choice == "Yes":
    social_points += 5
    study_hours += 3
    stress_level -= 2
    current_gpa += 0.1
    print("Coffee saved the day! You feel refreshed and socialized.")
else:
    study_hours += 5
    print("You skipped the coffee and got extra study time instead.")

print("\nYour friend asks: 'Wanna go to a party instead of studying?'")
party_choice = "No"  # testing default
if party_choice == "Yes":
    social_points += 20
    study_hours -= 15
    stress_level -= 5
    current_gpa -= 0.3
    print("You had a blast! But your study time took a hit.")
else:
    study_hours += 10
    stress_level += 5
    current_gpa += 0.2
    print("You stayed disciplined. GPA boost incoming!")

extra_study = "yes"  # testing default
if extra_study.lower() == "yes":
    study_hours += 15
    stress_level += 10
    print("You push through the night. More study hours, but stress increases.")
else:
    stress_level -= 5
    print("You decide to rest instead. Less stress, but no extra study hours.")

print("\nBreaking News: Google recruiters are visiting your campus. Are you going?")
google_choice = "Yes"  # testing default
if google_choice == "Yes":
    social_points += 5
    current_gpa += 0.2
    print("Networking pays off! You left with new connections and more confidence.")
else:
    stress_level -= 5
    social_points -= 5
    print("You skipped it to relax. Less stress, but maybe a missed chance.")

print("\nSurprise! A pop quiz in class. Do you cram last night or wing it?")
quiz_choice = "Cram"  # testing default
if quiz_choice.lower() == "cram":
    study_hours += 5
    stress_level += 5
    current_gpa += 0.3
    print("The late-night grind paid off—you aced it!")
else:
    stress_level -= 2
    current_gpa -= 0.3
    print("You winged it and flopped. Ouch, GPA slipped.")

group_study = "yes"  # testing default
if group_study.lower() == "yes":
    study_hours += 10
    stress_level -= 10
    print("Studying with friends keeps stress down and helps you learn more.")
else:
    study_hours += 5
    print("You stick to solo studying. You cover material, but stress lingers.")

# ================== Final GPA calculation and endings ==================
# Use 'not' to check empty course list, and 'is not' to check None correctly.
if not course_grades:
    # If for some reason no grades recorded, carry over starting GPA.
    print("\nNo course grades recorded, carrying over your starting GPA.")
    final_gpa = current_gpa
else:
    total_points = 0
    total_courses = 0
    for grade in course_grades:
        # safe: check for None with 'is not' and exclude 0 with 'not in'
        if grade is not None and grade not in [0]:
            total_points += grade
            total_courses += 1
    final_gpa = total_points / total_courses if total_courses > 0 else current_gpa


git add knhill2_assignment_4.py README.md
git commit -m "Final assessment: final GPA calc & multiple endings"

# Final Stop (original wording)
print("\nFinal Stop: Checking your progress...")
print(f"Ending GPA: {final_gpa:.2f}, Study Hours: {study_hours}, Social Points: {social_points}, Stress: {stress_level}")
print(" You arrive at your final destination...")

# Endings now use final_gpa so multiple endings are reachable.
if final_gpa >= 3.7 and study_hours >= 45 and social_points >= 25 and stress_level <= 55:
    print("You have arrived at Valedictorian Vista: From the balcony of success, your future stretches beyond the horizon. Congrats on Chancellor's List, and your academic success this semester.")
elif 3.4 <= final_gpa < 3.7 and study_hours >= 35 and stress_level > 45:
    print("Welcome to Prestige Point: Where excellence is earned, despite all the stress, you did it. Congrats!")
elif final_gpa >= 3.0 and study_hours >= 25 and social_points < 25 and stress_level <= 30:
    print("Welcome to Easy Street: Where the sun is always shining, not a cloud in the sky, like you. You laid low, but made it. Congrats on Dean's List.")
elif social_points >= 40 and final_gpa < 3.2 and study_hours >= 20 and stress_level <= 40:
    print("You've arrived at Social SkyWalk: You built an amazing social network, but academics crumbled. You still have a chance!")
elif final_gpa < 2.5 and study_hours < 20 and social_points >= 25 and stress_level > 45:
    print("Welcome to Rebel Rock: The parties never stopped, but you did. You’ve hit academic probation.")
else:
    print("You navigated the semester with balance, not hitting any extreme outcomes, but progress was made.")











