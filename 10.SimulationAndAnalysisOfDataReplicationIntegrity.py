import random
import copy
import math
import numpy as np
import pandas as pd

#generating the data
def generate_data(n=15):
    data = []
    for i in range(1, n+1):
        zone_data = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(40, 180)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }
        data.append(zone_data)
    return data

#personalized rule
def personalize_data(data):
    # assume ODD roll → rotate by 3
    return data[3:] + data[:3]

# custom risk function
def custom_risk_score(metrics):
    total = metrics["traffic"] + metrics["pollution"] + metrics["energy"]
    return math.log(total)

# converting into dataframe
def convert_to_dataframe(data):
    rows = []
    for a in data:
        row = {
            "zone": a["zone"],
            "traffic": a["metrics"]["traffic"],
            "pollution": a["metrics"]["pollution"],
            "energy": a["metrics"]["energy"],
            "risk": custom_risk_score(a["metrics"])
        }
        rows.append(row)
    return pd.DataFrame(rows)

# manual correlation
def manual_correlation(c, d):
    mean_c = np.mean(c)
    mean_d = np.mean(d)
    numerator = np.sum((c - mean_c) * (d - mean_d))
    denominator = np.sqrt(np.sum((c - mean_c)**2) * np.sum((d - mean_d)**2))
    return numerator / denominator

# mutation function
def mutate_data(data):
    for d in data:
        # modify nested dictionary
        d["metrics"]["traffic"] += 10

        # append to history
        d["history"].append(random.randint(100, 200))

# analysis
def analyze(df):
    mean = df["risk"].mean()
    std = df["risk"].std()
    anomalies = df[df["risk"] > mean + std]
    variance = np.var(df["risk"])
    stability_index = 1 / variance if variance != 0 else 0
    max_risk = df["risk"].max()
    min_risk = df["risk"].min()
    return anomalies, (max_risk, min_risk, stability_index)

# cluster detection
def detect_clusters(df, threshold):
    clusters = []
    current = []
    for i, row in df.iterrows():
        if row["risk"] > threshold:
            current.append(row["zone"])
        else:
            if len(current) > 1:
                clusters.append(current)
            current = []
    if len(current) > 1:
        clusters.append(current)

    return clusters

# final decision
def final_decision(stability, anomalies_count):
    if stability > 1 and anomalies_count == 0:
        return "System Stable"
    elif anomalies_count < 3:
        return "Moderate Risk"
    elif anomalies_count < 7:
        return "High Corruption Risk"
    else:
        return "Critical Failure"

# main function
data = generate_data()
data = personalize_data(data)

# Copies
assignment_copy = data
shallow_copy = copy.copy(data)
deep_copy = copy.deepcopy(data)

print("\nBefore mutation:")
print("Original[0]:", data[0])

# Mutate shallow copy
mutate_data(shallow_copy)

# After mutation
print("After mutation:")
print("Original[0]:", data[0])
print("Shallow[0]:", shallow_copy[0])
print("Deep[0]:", deep_copy[0])

# Convert to DataFrame
df = convert_to_dataframe(data)
print("\nDataframe:")
print(df)

# Analysis
anomalies, stats = analyze(df)
print("\nAnomalies:")
print(anomalies)

print("\nStats(max, min, stability_index):",stats)

# Manual correlation
corr = manual_correlation(df["traffic"].values, df["pollution"].values)
print("\nManual correlation(traffic vs pollution):",corr)

# Cluster detection
threshold = df["risk"].mean()
clusters = detect_clusters(df, threshold)
print("\nClusters:")
print(clusters)

# Final decision
decision = final_decision(stats[2], len(anomalies))
print("\nFinal decision:",decision)
