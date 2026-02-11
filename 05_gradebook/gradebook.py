last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]] 

# This semester's subjects and grades
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 98])

gradebook.remove(["poetry", 85])
gradebook.append(["poetry", "Pass"])

print("Last Semester's Grades\n")
print(last_semester_gradebook)

print("\nThis Semester's Grades\n")
print(gradebook)

print("\nFull Gradebook\n")
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)




