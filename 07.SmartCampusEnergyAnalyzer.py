energy_list = input("Enter energy readings separated by space: ")

readings = [int(a) for a in energy_list.split()]
categories = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

# categorizing the units in different categories
for energy in readings:
    if energy < 0:
        categories["invalid"].append(energy)
    elif energy >= 0 and energy <= 50:
        categories["efficient"].append(energy)
    elif energy >= 51 and energy <= 150:
        categories["moderate"].append(energy)
    else:
        categories["high"].append(energy)

#counting valid readings and total energy
valid_readings = [a for a in readings if a >= 0]
total = sum(valid_readings)
buildings_count = len(valid_readings)
summary = (total, buildings_count)

#usage pattern
result = ""

# Personalized Logic
if buildings_count > 0 and len(categories["efficient"]) > buildings_count / 2:
    result = "Highly Efficient Campus"

elif len(categories["high"]) > 3:
    result = "Overconsumption"
elif abs(len(categories["efficient"]) - len(categories["moderate"])) <= 1:
    result = "Balanced Usage"
elif total > 600:
    result = "Energy Waste Detected"
else:
    result = "Moderate Usage"

# final output
print("Categorized Readings:", categories)
print("Total Consumption:", summary[0])
print("Number of Buildings:", summary[1])
print("Result:", result)