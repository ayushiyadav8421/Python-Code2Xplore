n=int(input("Enter the number of students: "))
marks=[0]*n

section=input("Enter section:")

total_valid=0
total_failed=0
for j in range(n):
    marks[j]=int(input("Enter marks for student:"))
for i in range(n):
    if marks[i]<0 or marks[i]>100:
        print("Invalid")
    else:
        total_valid+=1

        if section=='J':
            if marks[i]<=39 and marks[i]>=35:
                marks[i]+=5;

        if marks[i]<=100 and marks[i]>=90:
            print(marks[i],"->" ,"Excellent")
        elif marks[i]<=89 and marks[i]>=75:
            print(marks[i], "->", "Very Good")
        elif marks[i]<=74 and marks[i]>=60:
            print(marks[i], "->", "Good")
        elif marks[i]<=59 and marks[i]>=40:
            print(marks[i], "->", "Average")
        else:
            print(marks[i],"->","Fail")
            total_failed+=1
print("Total valid students: ",total_valid)
print("Total failed students: ",total_failed)
