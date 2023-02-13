# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
  else:
    highest_score = highest_score

print(f"The highest score is {highest_score}")

# Code for minumum/lowest number
"""
lowest_score = 0
for score in student_scores:
  if score < lowest_score:
    lowest_score = score
  else:
    lowest_score = lowest_score

print(f"The highest score is {lowest_score}")
"""