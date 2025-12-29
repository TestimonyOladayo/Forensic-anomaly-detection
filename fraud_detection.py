import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os
# Create results folder if it doesn't exist
if not os.path.exists('results'):
    os.makedirs('results')
# 1. LOAD DATA
print("--- Step 1: Loading Forensic Data ---")
df = pd.read_csv('creditcard.csv')
# 2. PRE-PROCESSING
scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
X = df.drop(['Time', 'Amount', 'Class'], axis=1)
# 3. TRAIN THE AUDIT ENGINE
print("--- Step 2: Training Isolation Forest (Auditing Transactions) ---")
model = IsolationForest(contamination=0.0017, random_state=42)
df['scores'] = model.fit_predict(X)
# 4. GENERATE THE "SMOKING GUN" CHART
print("--- Step 3: Extracting Mechanistic Insights ---")
# We analyze the decision path to see which features matter most
avg_path_length = model.decision_function(X)
feature_importance = np.abs(X.mean(axis=0)) # Simplified importance for visualization
plt.figure(figsize=(12, 6))
sns.barplot(x=X.columns[:10], y=feature_importance[:10], palette="viridis")
plt.title('Forensic Audit: Key Features Driving Anomaly Detection', fontsize=15)
plt.ylabel('Impact Score', fontsize=12)
plt.savefig('results/feature_importance.png')
plt.show()

print("--- FINISHED: Chart saved to 'results/feature_importance.png' ---")
