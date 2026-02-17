n= int(input("enter size of list of weights:"))
weights=[0]*n
for i in range(n):
    weights[i]= int(input("enter weight:"))
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]

total_valid_weights=0
total_affected=0
for i in weights:
    if i<0:
        invalid_entries = invalid_entries+[i]
    elif i>=0 and i<=5:
        very_light= very_light+[i]
        total_valid_weights+=1
    elif i>=6 and i<=25:
        normal_load= normal_load+[i]
        total_valid_weights+=1
    elif i>=26 and i<=60:
        heavy_load= heavy_load+[i]
        total_valid_weights+=1
    else:
        overload= overload+[i]
        total_valid_weights+=1

# Personalized Logic
name=input("enter name:")
count_space=0
for char in name:
    if char==" ":
        count_space+=1
L=len(name)-count_space
PLI= L%3
if PLI==0:
    for item in overload:
        invalid_entries= invalid_entries+ [item]
        total_affected+=1
    overload=[]
if PLI==1:
    for item in normal_load:
        total_affected+=1
    normal_load=[]
if PLI==2:
    for item in very_light:
        total_affected+=1
    for item in normal_load:
        total_affected+=1
    for item in invalid_entries:
        total_affected+=1
    very_light=[]
    normal_load=[]
    invalid_entries=[]

print("Total valid weights:",total_valid_weights)
print("Total affected items due to PLI:",total_affected)
print("L:",L)
print("PLI:",PLI)
print("Very light:",very_light)
print("Normal load:",normal_load)
print("Heavy load:",heavy_load)
print("Overload:",overload)
print("Invalid entries:",invalid_entries)


