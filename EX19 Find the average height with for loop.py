# Find the average height
# You can not use SUM and LEN function
# Use only for loop

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

counter = 0
summ = 0
for n in student_heights:
    summ += n

for i in student_heights:
    counter += 1

average_height = round(summ / counter)
print(average_height)




