#1. Python List Transformation
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#sort grades in descending form 
grades.sort(reverse=True)
print(grades)
#find length of list to find average
print (len(grades))
total_sum = sum(grades) 
average = total_sum / 10 # calculated total of grades to get average when "/" by the nums of values in list
print (int(average)) #<< average grade = 84

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
print(grades)

# 2. Advanced List Methods and Identity Operators
    # Task 1: find students both submitted their assignments and attended the class.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted_attended = [ ]
for i in submitted:
    if i in attended:
        submitted_attended.append(i)

print (submitted_attended)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
sorted_submit = sorted(submitted)
sorted_attend = sorted(attended)
if sorted_submit == sorted_attend:
    print("They are identical")
else:
    print("They are not identical")

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]  
kick = [name for name in attended if name in submitted]
print(kick)

# 3. Advanced Slicing Techniques
    # Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

week2 = temperatures[7:14]
print(week2)

# Task 2: Extract all the temperatures above 100.
high = temperatures [-7:]
print(high)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures.reverse()
print(temperatures)
flipped = temperatures[4:10]
print(flipped)

# 4. Deep Dive into Python Lists
    # Task 1: Given the lists:
students = ["John",       "Doe",   "Jane",  "Smith"]
grades = [       85    ,         90,       78,        88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(students)):
    name = students[i]
    number = grades[i]
    subject = activities[i]
    if number < 80:
        print(f"{name}, {number}, {subject} ")

# Task 2: For the remaining students, add students name in a new list named students_approved.
students = ["John",       "Doe",   "Jane",  "Smith"]
grades = [       85    ,         90,       78,        88]
activities = ["Football", "Music", "Art", "Dance"]
for i in range(len(students)):
    name = students[i]
    number = grades[i]
    subject = activities[i]
    students_approved = name 
    if number > 80:
        # Task 3: Print the list students_approved
        print(students_approved, "is approved!")
