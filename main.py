# 180 124 165 173 189 169 146

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for items in student_heights:
  total_height += items

num_of_students = 0
for student in student_heights:
    num_of_students += 1

# average = total_height/(n+1)
average_height = round(total_height/num_of_students)

# print(round(average))
print(round(average_height))



