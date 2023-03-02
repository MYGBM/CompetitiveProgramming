n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        # Returns Name and line as separate
        # print(name)
        # print(line) 
        #Convert line to scores: a list containing floats
        scores = list(map(float, line))
        #Add the key value pairs, 'name':[scores]
        student_marks[name]=scores
query_name = input()
average=0
#access the value from key given if key exists in student_marks dictionary
score=student_marks.get(query_name)
for grade in score:
        average+=grade
average=average/3
print(format(average,'.2f'))






