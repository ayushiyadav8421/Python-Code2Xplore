import random
import numpy as np
import pandas as pd
import math

def generate_data(n=17):
    a=[]
    for i in range(n):
        record={
            "zone": i + 1,
            "traffic":random.randint(0, 100),
            "air_quality":random.randint(0, 300),
            "energy":random.randint(0, 500)
        }
        a.append(record)
    return a

# Classifying the data based on the given condition
def classifying_zone(record):
    if record["air_quality"]>200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

# calculating the risk
def risk_score(record):
    return (record["traffic"] * 0.4 +
            record["air_quality"] * 0.4 +
            record["energy"] * 0.2)

# sorting the data
def sort(a):
    #using bubble sort
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j]["traffic"] > a[j + 1]["traffic"]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Processing the data
def process_data(data, roll_number):
    # Personalized Rule
    if roll_number % 3 == 0:
        random.shuffle(data)
    else:
        data = sort(data)

    # Classification + Risk
    for record in data:
        record["category"] = classifying_zone(record)
        record["risk_score"] = risk_score(record)
        record["log_risk"] = math.log(record["risk_score"] + 1)

    return data

# Analysis using pandas and numpy
def analyze(data):
    df = pd.DataFrame(data)

    print("\nDataFrame:")
    print(df)

    print("\nCategorized Zones:")
    print(df[["zone", "category"]])
    zones_set = set(df["zone"])
    print("\nUnique Zones (Set):", zones_set)

    print("\nMean Values:")
    print(df[["traffic", "air_quality", "energy"]].mean())

    # Top three worst zones
    sorted_data = sorted(data, key=lambda x: x["risk_score"], reverse=True)
    top3 = sorted_data[:3]  #using slicing

    print("\nTop three risk zones:")
    for z in top3:
        print(f"Zone {z['zone']} → Risk Score: {z['risk_score']:.2f}")

    risks = df["risk_score"].values
    result_tuple = (np.max(risks), np.mean(risks), np.min(risks))
    print("\n(max_risk, avg_risk, min_risk):")
    print(result_tuple)
    return df, result_tuple

# Detecting patterns
def detect_patterns(df):
    threshold = df["risk_score"].mean()

    high_risk = df[df["risk_score"] > threshold]
    print("\nHigh Risk Zones:")
    print(high_risk[["zone", "risk_score"]])

    # Stability
    if np.var(df["traffic"]) < 500:
        print("\nTraffic is Stable")
    else:
        print("\nTraffic is Unstable")

    # Consecutive high-risk zones
    print("\nCritical Clusters:")
    count = 0
    for r in df["risk_score"]:
        if r > threshold:
            count += 1
            if count >= 2:
                print("Cluster detected")
        else:
            count = 0
    print("\nAQI Rising Zones:")
    for i in range(1, len(df)):
        if df["air_quality"][i] > df["air_quality"][i - 1]:
            print(f"Zone {df['zone'][i]} AQI rising")

# final decision
def final_decision(avg_risk):
    if avg_risk < 100:
        return "City Stable"
    elif avg_risk < 200:
        return "Moderate Risk"
    elif avg_risk < 300:
        return "High Alert"
    else:
        return "Critical Emergency"

def main():
    roll_number = 720

    data = generate_data()
    processed = process_data(data, roll_number)

    df, result_tuple = analyze(processed)

    detect_patterns(df)

    decision = final_decision(result_tuple[1])

    print("\nFinal Decision:", decision)

    # Unique Insight
    print("\nSmart City Insight:",end=" ")
    print("A smart city balances traffic, pollution, and energy efficiently using data-driven decisions.")

main()