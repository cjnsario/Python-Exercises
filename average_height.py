# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total_height = 0
total_number = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_height += student_heights[n]
  total_number += 1

print(f"The total height is {total_height}")
print(f"The total number is {total_number}")

average_height = round(total_height/total_number)
print(f"The average height is {average_height}")



# 🚨 Don't change the code above 👆


#Write your code below this row 👇




