student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height

average_height = round(total_height / len(student_heights))

print(f"Total height = {total_height}\nNumber of students = {len(student_heights)}\nAverage height = {average_height}")
