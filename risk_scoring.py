# import os
# print("Current working directory:", os.getcwd())
#
# import pandas as pd
# alerts = pd.read_csv("data/alerts.csv")
# assets = pd.read_csv("data/assets.csv")
# users = pd.read_csv("data/users.csv")
# historical_fp = pd.read_csv("data/historical_fp.csv")
# print(alerts)
# print(assets)
# print(users)
# print(historical_fp)
# alerts_assets = pd.merge(
#     alerts,
#     assets,
#     on="asset_id",
#     how="left"
# )
# print(alerts_assets)
# alerts_assets_users = pd.merge(
#     alerts_assets,
#     users,
#     on="user_id",
#     how="left"
# )
# print(alerts_assets_users)
# alerts_full = pd.merge(
#     alerts_assets_users,
#     historical_fp,
#     on="alert_type",
#     how="left"
# )
# print(alerts_full)
# # STEP 10: Normalize categorical risk factors
#
# asset_criticality_map = {
#     "Low": 1,
#     "Medium": 2,
#     "High": 3
# }
#
# alert_severity_map = {
#     "Low": 1,
#     "Medium": 2,
#     "High": 3
# }
#
# user_role_map = {
#     "Standard": 1,
#     "Privileged": 2,
#     "Admin": 3
# }
#
# #alerts_full["asset_score"] = alerts_full["asset_criticality"].map(asset_criticality_map)
# #alerts_full["severity_score"] = alerts_full["alert_severity"].map(alert_severity_map)
# #alerts_full["user_score"] = alerts_full["user_role"].map(user_role_map)
# print("Columns in alerts_full:", alerts_full.columns.tolist())
# # ----------------------------
# # STEP: Create scores for SOC risk
# # ----------------------------
#
# # asset_score: already numeric, just copy business_criticality
# alerts_full["asset_score"] = alerts_full["business_criticality"]
#
# # severity_score: map threat_severity strings to numeric
# alert_severity_map = {
#     "Critical": 5,
#     "High": 4,
#     "Medium": 3,
#     "Low": 1
# }
# alerts_full["severity_score"] = alerts_full["threat_severity"].map(alert_severity_map)
#
# # user_score: map role to numeric
# user_role_map = {
#     "Admin": 5,
#     "Standard User": 3,
#     "Service Account": 4,
#     "Guest": 1
# }
# alerts_full["user_score"] = alerts_full["role"].map(user_role_map)
#
# # Check the first few rows to confirm
# print(alerts_full[["business_criticality", "asset_score", "threat_severity", "severity_score", "role", "user_score"]].head())
#
# # ----------------------------
# # STEP: SOC Risk Scoring - Final Block
# # ----------------------------
#
# # 1️⃣ Asset Score (already numeric)
# alerts_full["asset_score"] = alerts_full["business_criticality"]
#
# # 2️⃣ Severity Score mapping
# alert_severity_map = {
#     "Critical": 5,
#     "High": 4,
#     "Medium": 3,
#     "Low": 1
# }
# alerts_full["severity_score"] = alerts_full["threat_severity"].map(alert_severity_map)
#
# # 3️⃣ User Score mapping
# user_role_map = {
#     "Admin": 5,
#     "Standard User": 3,
#     "Service Account": 4,
#     "Guest": 1
# }
# alerts_full["user_score"] = alerts_full["role"].map(user_role_map)
#
# # 4️⃣ Overall Risk Score (weighted)
# # Example weights: asset 40%, severity 40%, user 20%
# alerts_full["overall_risk_score"] = (
#     alerts_full["asset_score"] * 0.4 +
#     alerts_full["severity_score"] * 0.4 +
#     alerts_full["user_score"] * 0.2
# )
#
# # 5️⃣ Risk Band Assignment
# def assign_risk_band(score):
#     if score >= 4.5:
#         return "Critical"
#     elif score >= 3.5:
#         return "High"
#     elif score >= 2.5:
#         return "Medium"
#     else:
#         return "Low"
#
# alerts_full["risk_band"] = alerts_full["overall_risk_score"].apply(assign_risk_band)
#
# # 6️⃣ Preview the results
# print(alerts_full[[
#     "asset_score", "severity_score", "user_score", "overall_risk_score", "risk_band"
# ]].head())
#
# # 7️⃣ Export final DataFrame to CSV
# alerts_full.to_csv("risk_scored_alerts.csv", index=False)
# print("Risk scoring completed. CSV file saved as 'risk_scored_alerts.csv'.")
#
# # ----------------------------
# # SOC Risk-Based Scoring Project - Complete Script
# # ----------------------------
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # ----------------------------
# # 1️⃣ Load / Merge DataFrames
# # (Replace these lines with your actual CSV paths)
# # ----------------------------
# alerts_df = pd.read_csv(r"C:\Users\yashs\OneDrive - laurentian.ca\Desktop\risk_based_soc_project\alerts.csv")
# assets_df = pd.read_csv(r"C:\Users\yashs\OneDrive - laurentian.ca\Desktop\risk_based_soc_project\assets.csv")
# users_df = pd.read_csv(r"C:\Users\yashs\OneDrive - laurentian.ca\Desktop\risk_based_soc_project\users.csv")
#
#
# # Merge alerts with asset and user info
# alerts_full = pd.merge(alerts_df, assets_df, on="asset_id", how="left")
# alerts_full = pd.merge(alerts_full, users_df, on="user_id", how="left")
#
# # Preview columns
# print("Columns in alerts_full:", alerts_full.columns.tolist())
#
# # ----------------------------
# # 2️⃣ Create Scores
# # ----------------------------
#
# # Asset Score (business_criticality is already numeric)
# alerts_full["asset_score"] = alerts_full["business_criticality"]
#
# # Severity Score mapping
# alert_severity_map = {
#     "Critical": 5,
#     "High": 4,
#     "Medium": 3,
#     "Low": 1
# }
# alerts_full["severity_score"] = alerts_full["threat_severity"].map(alert_severity_map)
#
# # User Score mapping
# user_role_map = {
#     "Admin": 5,
#     "Standard User": 3,
#     "Service Account": 4,
#     "Guest": 1
# }
# alerts_full["user_score"] = alerts_full["role"].map(user_role_map)
#
# # Preview scoring
# print(alerts_full[["business_criticality", "asset_score", "threat_severity", "severity_score", "role", "user_score"]].head())
#
# # ----------------------------
# # 3️⃣ Overall Risk Score
# # Weighted: asset 40%, severity 40%, user 20%
# # ----------------------------
# alerts_full["overall_risk_score"] = (
#     alerts_full["asset_score"] * 0.4 +
#     alerts_full["severity_score"] * 0.4 +
#     alerts_full["user_score"] * 0.2
# )
#
# # ----------------------------
# # 4️⃣ Risk Band Assignment
# # ----------------------------
# def assign_risk_band(score):
#     if score >= 4.5:
#         return "Critical"
#     elif score >= 3.5:
#         return "High"
#     elif score >= 2.5:
#         return "Medium"
#     else:
#         return "Low"
#
# alerts_full["risk_band"] = alerts_full["overall_risk_score"].apply(assign_risk_band)
#
# # Preview overall risk and bands
# print(alerts_full[["overall_risk_score", "risk_band"]].head())
#
# # ----------------------------
# # 5️⃣ Export Final DataFrame to CSV
# # ----------------------------
# alerts_full.to_csv("risk_scored_alerts.csv", index=False)
# print("Risk scoring completed. CSV saved as 'risk_scored_alerts.csv'.")
#
# # ----------------------------
# # 6️⃣ Visualizations
# # ----------------------------
#
# # 6a. Bar chart: number of alerts per risk band
# plt.figure(figsize=(8,5))
# sns.countplot(x="risk_band", data=alerts_full, order=["Low", "Medium", "High", "Critical"], palette="Reds_r")
# plt.title("Number of Alerts by Risk Band")
# plt.xlabel("Risk Band")
# plt.ylabel("Number of Alerts")
# plt.show()
#
# # 6b. Correlation heatmap of scores
# numeric_cols = ["asset_score", "severity_score", "user_score", "overall_risk_score"]
# plt.figure(figsize=(6,5))
# sns.heatmap(alerts_full[numeric_cols].corr(), annot=True, cmap="Reds", fmt=".2f")
# plt.title("Correlation Heatmap of Risk Scores")
# plt.show()
#
# # 6c. Scatter plot: overall risk vs severity, colored by risk band
# plt.figure(figsize=(8,5))
# sns.scatterplot(
#     x="severity_score",
#     y="overall_risk_score",
#     hue="risk_band",
#     data=alerts_full,
#     palette="Reds_r",
#     s=100
# )
# plt.title("Overall Risk vs Severity Score")
# plt.xlabel("Severity Score")
# plt.ylabel("Overall Risk Score")
# plt.legend(title="Risk Band")
# plt.show()

# -------------------------------
# risk_scoring.py
# SOC Risk-Based Alert Scoring Script
# Works with alerts.csv, assets.csv, users.csv
# -------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Step 1: Define folder and CSV paths
# -------------------------------
csv_folder = r"C:\risk_project"  # <- All CSVs here

alerts_path = os.path.join(csv_folder, "alerts.csv")
assets_path = os.path.join(csv_folder, "assets.csv")
users_path = os.path.join(csv_folder, "users.csv")

# -------------------------------
# Step 2: Check if files exist
# -------------------------------
for f in [alerts_path, assets_path, users_path]:
    if not os.path.exists(f):
        print(f"\nERROR: File not found: {f}")
        exit(1)

# -------------------------------
# Step 3: Read CSVs
# -------------------------------
alerts_df = pd.read_csv(alerts_path)
assets_df = pd.read_csv(assets_path)
users_df = pd.read_csv(users_path)

# -------------------------------
# Step 4: Merge data
# -------------------------------
alerts_full = alerts_df.merge(assets_df, on="asset_id", how="left")
alerts_full = alerts_full.merge(users_df, on="user_id", how="left")

# -------------------------------
# Step 5: Scoring maps
# -------------------------------
asset_criticality_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
alert_severity_map = {"Low": 1, "Medium": 3, "High": 4, "Critical": 5}
user_role_map = {"Standard User": 3, "Admin": 5, "Service Account": 4}

# Map scores
alerts_full["asset_score"] = alerts_full["business_criticality"].map(asset_criticality_map)
alerts_full["severity_score"] = alerts_full["threat_severity"].map(alert_severity_map)
alerts_full["user_score"] = alerts_full["role"].map(user_role_map)

# -------------------------------
# Step 6: Calculate risk score and band
# -------------------------------
alerts_full["risk_score"] = 0.4 * alerts_full["asset_score"] + \
                            0.4 * alerts_full["severity_score"] + \
                            0.2 * alerts_full["user_score"]

def risk_band(score):
    if score >= 4.5:
        return "Critical"
    elif score >= 3.5:
        return "High"
    elif score >= 2.5:
        return "Medium"
    else:
        return "Low"

alerts_full["risk_band"] = alerts_full["risk_score"].apply(risk_band)

# -------------------------------
# Step 7: Save risk-scored CSV
# -------------------------------
output_csv_path = os.path.join(csv_folder, "risk_scored_alerts.csv")
alerts_full.to_csv(output_csv_path, index=False)
print(f"\nRisk scoring completed. CSV saved at '{output_csv_path}'")

# -------------------------------
# Step 8: Interactive filtering
# -------------------------------
departments = alerts_full["department"].unique()
asset_types = alerts_full["asset_type"].unique()

print("\nAvailable departments:")
for i, d in enumerate(departments, 1):
    print(f"{i}. {d}")

print("\nAvailable asset types:")
for i, a in enumerate(asset_types, 1):
    print(f"{i}. {a}")

# Prompt user to select
dept_input = input("\nEnter department name from the above list: ")
asset_input = input("Enter asset type from the above list: ")

# Filter based on user input
filtered_alerts = alerts_full[
    (alerts_full["department"] == dept_input) &
    (alerts_full["asset_type"] == asset_input)
]

if filtered_alerts.empty:
    print(f"\nNo alerts found for Department='{dept_input}' and Asset Type='{asset_input}'.")
else:
    print(f"\nFiltered alerts for Department='{dept_input}' and Asset Type='{asset_input}':")
    print(filtered_alerts[["alert_id", "asset_score", "severity_score", "user_score", "risk_score", "risk_band"]].head(10))

    # Visualize risk bands for filtered alerts
    plt.figure(figsize=(6, 4))
    filtered_alerts["risk_band"].value_counts().plot(kind="bar", color="coral")
    plt.title(f"Risk Band Distribution ({dept_input} / {asset_input})")
    plt.xlabel("Risk Band")
    plt.ylabel("Count")
    plt.tight_layout()
    fig_path = os.path.join(csv_folder, f"risk_band_distribution_{dept_input}_{asset_input}.png")
    plt.savefig(fig_path)
    print(f"\nRisk band chart saved at '{fig_path}'")
    plt.show()

# -------------------------------
# Step 9: Full SOC Dashboard
# -------------------------------
print("\nGenerating full SOC risk dashboard...")

# Group by Department and Risk Band
dashboard_dept = alerts_full.groupby(["department", "risk_band"]).size().unstack(fill_value=0)
dashboard_dept.plot(kind="bar", stacked=True, figsize=(8, 5), colormap="coolwarm")
plt.title("SOC Risk Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Number of Alerts")
plt.tight_layout()
plt.savefig(os.path.join(csv_folder, "soc_risk_dashboard_department.png"))
plt.show()

# Group by Asset Type and Risk Band
dashboard_asset = alerts_full.groupby(["asset_type", "risk_band"]).size().unstack(fill_value=0)
dashboard_asset.plot(kind="bar", stacked=True, figsize=(8, 5), colormap="viridis")
plt.title("SOC Risk Distribution by Asset Type")
plt.xlabel("Asset Type")
plt.ylabel("Number of Alerts")
plt.tight_layout()
plt.savefig(os.path.join(csv_folder, "soc_risk_dashboard_asset_type.png"))
plt.show()

print("\nFull SOC dashboard generated and saved as PNG files.")
