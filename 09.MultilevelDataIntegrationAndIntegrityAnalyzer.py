import copy

# generates data(user input)
def generate_data():
    users = []
    n = int(input("Enter number of users: "))
    for i in range(n):
        user_id = int(input(f"Enter ID for user {i+1}: "))

        file_count = int(input("Enter number of files: "))
        files = []
        for j in range(file_count):
            file_name = input(f"Enter file {j+1}: ")
            files.append(file_name)

        usage = int(input("Enter usage: "))

        users.append({
            "id": user_id,
            "data": {"files": files, "usage": usage}
        })
    return users

# replication
def replicate_data(users):
    assigned = users
    shallow = copy.copy(users)      #shallow copy
    deep = copy.deepcopy(users)     #deep copy
    return assigned, shallow, deep

# Modifying the data
def modify_data(data, roll_number):
    for user in data:

        #personalized mutation logic
        if roll_number % 2 == 0:                # add one file
            user["data"]["files"].append("new_file.txt")
        else:                                   # delete one file
            if user["data"]["files"]:
                user["data"]["files"].pop()

        user["data"]["usage"] += 100

# checking integrity
def check_integrity(org, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    for i in range(len(org)):
        orig_files = set(org[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])

        if orig_files != shallow_files:
            leakage_count += 1

        if orig_files != deep_files:
            safe_count += 1

        overlap = orig_files.intersection(shallow_files)
        overlap_count += len(overlap)

    return (leakage_count, safe_count, overlap_count)

# main
users = generate_data()
print("BEFORE:", users)

assigned, shallow, deep = replicate_data(users)
roll_number = int(input("\nEnter your roll number: "))

# modify shallow copy
modify_data(shallow, roll_number)

print("\nAFTER MODIFICATION:")
print("Original:", users)
print("Shallow:", shallow)
print("Deep:", deep)

# Integrity report
report = check_integrity(users, shallow, deep)

print("\nIntegrity Report (leakage, safe, overlap):", report)

print("Why inner list got affected?")
print("In shallow copy, only the outer list is copied, but inner objects (like 'files' list"
      " still refer to the same memory location.)")
print("So when we modify the inner list in shallow copy, it also changes the original data.")

print("\nDeep Copy Behavior:")
print("Deep copy creates completely independent copies of all nested objects,"
      " so changes in deep copy do not affect the original.")

print("\nAssignment Behavior:")
print("Assignment does not create a copy; it just creates another reference to the same data.")