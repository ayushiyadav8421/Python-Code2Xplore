n=int(input("Enter the size of the list:"))
lists=[0]*n
number_count=0
string_count=0
number_list=[0]*n
string_list=[0]*n
for i in range(n):
    lists[i]= input("Enter the list content:")
    if lists[i]==' ':
        continue
    if lists[i].isdigit():
        number_list[number_count]=int(lists[i])
        number_count+=1
    else:
        string_list[string_count]=lists[i]
        string_count+=1
# Personalization logic(section logic)
section=input("Enter your section:")
if section=='A':
    print("Number list:",number_list[:number_count])
    print("Number count:", number_count)

elif section=="B":
    print("String list:",string_list[:string_count])
    print("String count:", string_count)
elif section=='C':
    print("Number list:", number_list[:number_count])
    print("string list:", string_list[:string_count])
    print("Number count:", number_count)
    print("String count:", string_count)
else:
    print("Invalid section")


