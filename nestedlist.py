#Appending name and marks to a result list
n=input('enter number of students >: ')
res=[]
grades=[]
for i in range(int(n)):
     name=input(f'enter {i+1} name: ')
     mark=float(input(f'enter {i+1} mark: '))
     res.append([name,mark])
     grades.append(mark)
#print(res) 
#print(grades)

# Task 2 Method 1 sort then convert to set
new_grades=sorted(set(grades))
second_lowest=new_grades[1]

# Task 2 Method 2
# #print grades- unsorted 
# grades.sort()
# #print(grades) - sorted
# minimun_val=grades[0]
# for grade in grades:
#     if grade>minimun_val:
#         break
# second_lowest=grade
# #print(second_lowest)- second_lowest grade




#Task 3 get names from res list
names=[]
for name,mark in res:
    if second_lowest ==mark:
        names.append(mark)
# for value in res:
#         if second_lowest ==value[1]:
#             names.append(value[0])

#Task 4 sort names in alphabetical order
names.sort()
for name in names:
    print(name)